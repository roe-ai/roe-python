# Roe AI Agents Builder

Build, deploy, and share AI Agents in no time.

## Package Build
For testing, register a test PyPI account to get the API token:
https://test.pypi.org/account/register/

Run the following commands:
```
pip install -r requirements.txt
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```
You will be prompted for a username and password. For the username, use `__token__`. For the password, use the token value, including the `pypi-` prefix.

Installing the testing package:
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps roe-ai
```