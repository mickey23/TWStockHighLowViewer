import requests

TOKEN = "8147052824:AAGkxfP0eV0tEWnn9CNvbiH-BpltPWTqoMw"
CHAT_ID = "1046325808"

def send_message(msg):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })
