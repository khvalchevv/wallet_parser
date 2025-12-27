from telethon import TelegramClient, events

api_id = 22056618  # встав свій
api_hash = 'db2bf3b16f1788d38091014befe31c0d'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

# 📩 Джерела (як на скріні) — username БЕЗ "@"
SOURCE_CHAT_1 = 'EtherDROPSS_bot'
SOURCE_CHAT_2 = 'redactedsystemsbot'  # ти писав: @redactedsystemsbot

# 🎯 Куди шлеш (як на скріні)
TARGET_CHAT_ID = -1002604238211  # 📩 Група, куди шлеш

# 🧵 Яка гілка для якого джерела
SOURCE_TO_THREAD = {
    SOURCE_CHAT_1.lower(): 10845,
    SOURCE_CHAT_2.lower(): 6317,
}

@client.on(events.NewMessage(chats=[SOURCE_CHAT_1, SOURCE_CHAT_2]))
async def forward_message(event):
    try:
        src_username = (getattr(event.chat, 'username', '') or '').lower()
        thread_id = SOURCE_TO_THREAD.get(src_username)

        if not thread_id:
            return

        print(f"📩 Пересилаю в гілку {thread_id} (джерело: @{src_username})")
        await client.send_message(
            entity=TARGET_CHAT_ID,
            message=event.message,
            reply_to=thread_id
        )

    except Exception as e:
        print(f"❌ Error: {e}")

client.start()
print("✅ Слухаю повідомлення й пересилаю в гілки...")
client.run_until_disconnected()
