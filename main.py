import requests
import json
import time

# Load cookies from JSON
def load_cookies():
    with open("cookies.json", "r") as file:
        cookies_raw = json.load(file)
    cookies = {cookie['name']: cookie['value'] for cookie in cookies_raw}
    return cookies

# Optional: Telegram notification
def notify(msg):
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        url = f"https://api.telegram.org/bot{config['bot_token']}/sendMessage"
        payload = {
            "chat_id": config['chat_id'],
            "text": msg
        }
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)

# Check balance and basic info
def check_dashboard():
    url = "https://faucetcrypto.com/dashboard"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    cookies = load_cookies()
    response = requests.get(url, headers=headers, cookies=cookies)
    if "Welcome back" in response.text:
        print("✅ Logged in successfully.")
        notify("✅ Bot Logged in and running.")
    else:
        print("❌ Login failed or cookies expired.")
        notify("❌ Login failed or cookies expired.")

# Main loop
def main():
    while True:
        check_dashboard()
        print("⏳ Waiting before next check...")
        time.sleep(600)  # 10 minutes

if __name__ == "__main__":
    main()

