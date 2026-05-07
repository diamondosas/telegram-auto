from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from datetime import date
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

app_id= (os.getenv('APP_ID'))
app_hash = os.getenv('APP_HASH')
session_string=os.getenv('SESSION_STRING')
mummy_no = "+2349138305164"
message = f"Good Morning Ma. Welcome to {date.today()} I hope you had a good night sleep"

def prepare_message():
    response = requests.get("https://zenquotes.io/api/today")
    if response.status_code == 200:
        data = response.json()
        global message
        message += f"\n**Quote of the day**\n{data[0]['q']} - {data[0]['a']} "
        print("Quote Fetched")
    else:
        print("Failed to fetch quote")

def main():
    with TelegramClient(StringSession(session_string), app_id, app_hash) as client:
        client.send_message(mummy_no, message)

            
        print("message sent sucessfully")

if __name__ == "__main__":
    prepare_message()
    main()

