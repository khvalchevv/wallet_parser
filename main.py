from telethon import TelegramClient

api_id = 22056618  # встав свій
api_hash = 'db2bf3b16f1788d38091014befe31c0d'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

SOURCE_CHAT_ID = EtherDROPS5_bot  # 🔁 Група, звідки ловиш повідомлення
TARGET_CHAT_ID = -1009876543210  # 🔁 Група, куди шлеш
TARGET_THREAD_ID = 4567  # 🔁 Конкретна гілка в чаті

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_message(event):
    try:
        print(f"🔁 Пересилаю в гілку {TARGET_THREAD_ID}")
        await client.send_message(
            entity=TARGET_CHAT_ID,
            message=event.message,
            reply_to=TARGET_THREAD_ID
        )
    except Exception as e:
        print(f"❌ Error: {e}")

client.start()
print("✅ Слухаю повідомлення й пересилаю в гілку...")
client.run_until_disconnected()
