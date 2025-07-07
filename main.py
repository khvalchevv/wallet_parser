from telethon import TelegramClient, events

api_id = 22056618
api_hash = 'db2bf3b16f1788d38091014befe31c0d'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

# Джерело
SOURCE_BOT = 'EtherDROPS5_bot'

# Куди пересилати
TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 10845

@client.on(events.NewMessage(chats=SOURCE_BOT))
async def forward_message(event):
    try:
        await client.send_message(
            entity=TARGET_CHAT_ID,
            message=event.message,
            reply_to=TARGET_THREAD_ID  # Прибери цей рядок, якщо не потрібно в гілку
        )
    except Exception as e:
        print(f"❌ Error: {e}")

client.start()
print("✅ Бот слухає повідомлення від @EtherDROPS5_bot...")
client.run_until_disconnected()
