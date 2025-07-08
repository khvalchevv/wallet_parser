from telethon import TelegramClient, events

api_id = 22056618
api_hash = 'db2bf3b16f1788d38091014befe31c0d' 
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print(f"📥 NEW MESSAGE")
    print(f"From Chat ID: {event.chat_id}")
    print(f"Message: {event.raw_text}")

client.start()
print("✅ LISTENING...")
client.run_until_disconnected()
