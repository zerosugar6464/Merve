from LostMuzik import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**👤 Kullanıcı: {reply.from_user.first_name}\n 🆔 Kullanıcı ID**: `{reply.from_user.id}`\n**👥 Grup ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**👥 Grup ID**: `{message.chat.id}`"
        )
