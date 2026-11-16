import os
import requests

HANDLE = "ummigulsimks"
TARGET = 990
PRE_ALERT = 989

def send_message(message):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": message},
        timeout=30
    ).raise_for_status()

def main():
    url = f"https://pulse.walls.sh/profile?url=https://www.threads.com/@{HANDLE}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    followers = int(data["followers"])

    print("Followers:", followers)

    if followers >= PRE_ALERT:
        send_message(f"🔔 @{HANDLE} — {followers} жазылушы! 990-ға жақын!")

    if followers >= TARGET:
        send_message(f"🎉 ҚҰТТЫҚТАЙМЫН! @{HANDLE} 990-ға жетті!")

if __name__ == "__main__":
    main()
