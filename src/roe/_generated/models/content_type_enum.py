from enum import Enum

class ContentTypeEnum(str, Enum):
    APPLICATIONJSON = "application/json"
    APPLICATIONPDF = "application/pdf"
    AUDIO = "audio/*"
    AUDIOMP3 = "audio/mp3"
    AUDIOMPEG = "audio/mpeg"
    AUDIOWAV = "audio/wav"
    AUDIOX_M4A = "audio/x-m4a"
    IMAGE = "image/*"
    IMAGEJPEG = "image/jpeg"
    IMAGEPNG = "image/png"
    TEXT = "text/*"
    TEXTCSV = "text/csv"
    TEXTHTML = "text/html"
    TEXTMARKDOWN = "text/markdown"
    TEXTPLAIN = "text/plain"
    TEXTXML = "text/xml"
    VALUE_18 = "*/*"
    VIDEO = "video/*"
    VIDEOMP4 = "video/mp4"

    def __str__(self) -> str:
        return str(self.value)
