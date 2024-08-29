from AlexaMusic import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**🆔 Senin ID**: `{message.from_user.id}`\n**{reply.from_user.first_name} 👤 Kullanıcı ID**: `{reply.from_user.id}`\n**👥 Grup ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**🆔 Senin ID**: `{message.from_user.id}`\n**👥 Grup ID**: `{message.chat.id}`"
        )
