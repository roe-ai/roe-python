import os
import audioop
import base64
import json
from flask import Flask, request
from flask_sock import Sock
from twilio.twiml.voice_response import VoiceResponse, Connect
from google.cloud import texttospeech
from pydub import AudioSegment
from io import BytesIO
import openai
import wave
from examples.book_and_wiki import KnowledgeableAgent
from src.roe_ai.agent_input import PineconeInput, TextInput


app = Flask(__name__)
sock = Sock(app)
KNOWLEDGEABLE_AGENT = KnowledgeableAgent()
KNOWLEDGEABLE_AGENT.setup_cli()

openai.api_key = "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"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcp_secret.json'


@app.route("/voice", methods=["POST"])
def voice():
    """Accept a phone call."""
    response = VoiceResponse()
    connect = Connect()
    connect.stream(url=f'wss://{request.host}/stream')
    response.append(connect)
    print(f'Incoming call from {request.form["From"]}')
    return str(response), 200, {'Content-Type': 'text/xml'}


@sock.route('/stream')
def stream(ws):
    """Receive and transcribe audio stream."""
    
    silence_buffer = b''
    non_silence_buffer = b''
    silence_duration = 0
    non_silence_duration = 0
    messages = [
        {
            "role": "system",
            "content": "You are a very kind, warming person that does a casual chat with me. When speaking, keep it short in 2 sentences or so."
        }
    ]
    
    silence_duration = 0
    while True:
        message = ws.receive()
        packet = json.loads(message)
        print(packet)
        if packet['event'] == 'start':
            print('Streaming is starting')
        elif packet['event'] == 'stop':
            print('\nStreaming has stopped')
        elif packet['event'] == 'media':
            
            audio = base64.b64decode(packet['media']['payload'])
            audio = audioop.ulaw2lin(audio, 2)

             # Check for silence
            rms = audioop.rms(audio, 2)
            if rms < 300:
                silence_buffer += audio
                silence_duration += len(audio) / 16000
            else:
                non_silence_buffer += audio
                non_silence_duration += len(audio) / 16000
                silence_buffer = b''
                silence_duration = 0

            # Send the response if there is silence for more than 1 seconds
            # and the non-silence part is more than 1 second long
            if silence_duration >= 1 and non_silence_duration >= 0.5:
                with wave.open('recording.wav', 'w') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(8000)
                    wf.writeframes(non_silence_buffer)
                silence_buffer = b''
                non_silence_buffer = b''
                language = 'en'
                with open('recording.wav', 'rb') as f:
                    transcript = openai.Audio.transcribe("whisper-1", f, language=language, temperature=0)
                if transcript['text'] == '.' or transcript['text'] == '' or 'Amara.org' in transcript['text'] or '视频' in transcript['text']:
                    continue
                print(transcript['text'])
                messages.append({"role": "user", "content": transcript['text']})
                response = KNOWLEDGEABLE_AGENT.run(
                    {  
                        "pinecone": PineconeInput(
                            "cc4c64ff-e33a-4ab1-b54a-5a47505910ce", "gcp-starter", "gutenburg"
                        ),
                        "query": TextInput(
                            '\n'.join(msg['content'] for msg in messages if msg['role'] != 'system') + "\n respond in 3 sentences only."
                        ),
                    })
                messages.append({"role": "assistant", "content": response})
                media_data = {
                    "event": "media",
                    "streamSid": packet['streamSid'],
                    "media": {
                        "payload": text_to_speech(messages[-1]['content'])
                    }
                }
                
                media = json.dumps(media_data)
                print(media)
                ws.send(media)
                
                silence_duration = 0
                non_silence_duration = 0

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcp_secret.json'


def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Studio-O"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Convert MP3 data to PCM
    mp3_audio = AudioSegment.from_mp3(BytesIO(response.audio_content))
    pcm_audio = mp3_audio.set_frame_rate(8000).set_channels(1).set_sample_width(2)

    # Convert PCM data to u-law
    ulaw_audio = audioop.lin2ulaw(pcm_audio.raw_data, 2)

    # Base64 encode the u-law audio
    base64_audio = base64.b64encode(ulaw_audio).decode('utf-8')
    
    return base64_audio


if __name__ == '__main__':
    app.run(debug=True)
