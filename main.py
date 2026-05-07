from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from datetime import date

app_id= 35339131
app_hash = "360782156af3828ac885da8cee837c58"
session_string= "1BJWap1wBu0gLhRyAMkCBI5LwtKDT7o16GFA17srkx2M_m6Fzs08nyuX662p05wmlsggwW3pISixg4tgcWpbAz5EEn1YXgVu9_2xO8vAeHFrQ1rhhQ8_j9LExoEnCgQJ5aDYEbZQ_drPL9CZQlpQhWv-dw2NIa4_jhPpOGIWpdUkifCNiHk9FaumXQGT8Yv0nEPYGI73zePxBJrWAxuu9lqx2wp6IpBZm790VDk0YLZlCBCycxHKEaKzf2DujbK2DS1AFkxWgrOb7Bqu4Rl0B_4LN7QS4Xb1pQvOI8diR4saNT3byj5B7NeOlYm9u1YZ-uRHxRxMxfNw-jR23GIh-p5bR4P9aUGk="
mummy_no = "+2348034956959"
message = f"Good Morning Ma. Welcome to {date.today()} I hope you had a good night sleep"

def main():
    with TelegramClient(StringSession(session_string), app_id, app_hash) as client:
        client.send_message(mummy_no, message)
        print("message sent sucessfully")

if __name__ == "__main__":
    main()

