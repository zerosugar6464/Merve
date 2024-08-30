from pyrogram import Client, filters
from pyrogram.types import Message
from LostMuzik import app
from LostMuzik.utils.database import get_served_chats
from config import LOG_GROUP_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "Gizli Kullanıcı"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grup 🔒"
        lemda_text = f"#Yeni Gruba Eklendi..\n\n**Grup Adı**: {matlabi_jhanto}\n**Grup ID**: {chat_id}\n**Grup Linki**: {chatusername}\n**Toplam Grup**: {served_chats}\n**Ekleyen Kişi**: {added_by}"
        await lul_message(LOG_GROUP_ID, lemda_text)
