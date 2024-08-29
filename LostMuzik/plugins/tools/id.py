from LostMuzik import app
from pyrogram import Client, filters

from pyrogram.enums import ParseMode



@app.on_message(filters.command("id"))
async def _id(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    mesaj = message.reply_to_message or message
    text = f"""
**👤 Kullanıcı Adı:** {mesaj.from_user.mention if mesaj.from_user else None}
**🆔 Kullanıcı ID:** `{mesaj.from_user.id if mesaj.from_user else None}`
**📚 Kullanıcı Adı:** @{mesaj.from_user.username if mesaj.from_user else None}
"""
    await message.reply(text)

  
@app.on_message(filters.command("info"))
async def info(client: Client, message: Message):
    mesaj = message.reply_to_message or message
    chat = message.chat
    text = f"""
**👤 Kullanıcı Adı:** {mesaj.from_user.mention if mesaj.from_user else None}
**🆔 Kullanıcı ID:** `{mesaj.from_user.id if mesaj.from_user else None}`
**📚 Kullanıcı Adı:** @{mesaj.from_user.username if mesaj.from_user else None}

**👥 Grup Adı:** `{chat.title if chat else None}`
**🆔 Grup ID:** `{chat.id if chat else None}`
"""
    await message.reply(text)
