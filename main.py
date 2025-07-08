from telethon import TelegramClient

api_id = 22056618  # встав свій
api_hash = 'db2bf3b16f1788d38091014befe31c0d'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    try:
        # 🔁 Вкажи правильний цільовий chat ID (група або супергрупа)
        TARGET_CHAT_ID = -1002604238211
        await client.send_message(TARGET_CHAT_ID, "✅ Тест: юзербот може писати!")
        print("✅ Повідомлення надіслано!")
    except Exception as e:
        print(f"❌ Помилка надсилання: {e}")

with client:
    client.loop.run_until_complete(main())
