import requests

def post(url, message):
    requests.post(url, data=message.encode(encoding='utf-8'))