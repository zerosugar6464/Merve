import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

import config

from ..logging import LOGGER


private_commands = [
    BotCommand("start", "🎧 ʙᴏᴛᴜ ʙᴀşʟᴀᴛıʀ"),
    BotCommand("yardim", "📖 ʏᴀʀᴅıᴍ ᴍᴇɴᴜ̈sᴜ̈ɴᴜ̈ ɢᴏ̈sᴛᴇʀɪʀ"),
]


group_commands = [
    BotCommand("oynat", "🔼 ᴍᴜ̈ᴢɪɢ̆ɪ ᴏʏɴᴀᴛıʀ"),
    BotCommand("voynat", "📹 ᴠɪᴅᴇᴏʏᴜ ᴏʏɴᴀᴛıʀ"),
    BotCommand("atla", "⏭️ sᴏɴʀᴀᴋɪ ᴘᴀʀᴄ̧ᴀʏᴀ ɢᴇᴄ̧ᴇʀ"),
    BotCommand("duraklat", "⏸️ ᴄ̧ᴀʟᴀɴ ᴘᴀʀᴄ̧ᴀʏı ᴅᴜʀᴅᴜʀᴜʀ"),
    BotCommand("devam", "▶️ ᴄ̧ᴀʟᴀɴ ᴘᴀʀᴄ̧ᴀʏı ᴅᴇᴠᴀᴍ ᴇᴛᴛɪʀɪʀ"),
    BotCommand("son", "⏹️ ᴄ̧ᴀʟᴀɴ ᴘᴀʀᴄ̧ᴀʏı ᴋᴀᴘᴀᴛıʀ"),
    BotCommand("karistir", "🔀 ᴄ̧ᴀʟᴀɴ ᴘᴀʀᴄ̧ᴀʏı ᴋᴀʀışᴛıʀıʀ"),
    BotCommand("dongu", "🔄 ᴄ̧ᴀʟᴀɴ ᴘᴀʀᴄ̧ᴀʏı ᴛᴇᴋʀᴀʀʟᴀʀ"),
    BotCommand("sira", "📖 ᴄ̧ᴀʟᴍᴀ ʟɪsᴛᴇʟᴇʀɪɴɪ ɢᴏ̈sᴛᴇʀɪʀ"),
    BotCommand("ilerisar", "⏩ ᴘᴀʀᴄ̧ᴀʏı ɪ̇ʟᴇʀɪ̇ sᴀʀᴀʀ"),
    BotCommand("gerisar", "⏪ ᴘᴀʀᴄ̧ᴀʏı ɢᴇʀɪ sᴀʀᴀʀ"),
    BotCommand("playlist", "📖 ᴄ̧ᴀʟᴍᴀ ʟɪsᴛᴇɴɪᴢɪ ɢᴏ̈sᴛᴇʀɪʀ"),
    BotCommand("bul", "📩 sᴇᴄ̧ᴛɪɢ̆ɪɴɪᴢ ᴘᴀʀᴄ̧ᴀʏı ɪ̇ɴᴅɪ̇ʀɪ̇ʀ"),
    BotCommand("ayarlar", "⚙️ ʙᴏᴛ ᴀʏᴀʀʟᴀʀıɴı ɢᴏ̈sᴛᴇʀɪʀ"),
    BotCommand("restart", "🔃 ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛıʀ"),
    BotCommand("reload", "❤️‍🔥 ʏᴏ̈ɴᴇᴛɪᴄɪ ᴏ̈ɴʙᴇʟʟᴇɢ̆ɪɴɪ ɢᴜ̈ɴᴄᴇʟʟᴇʀ"),
    BotCommand("id", "🆔 ᴋᴜʟʟᴀɴıᴄı ɪᴅ'sɪɴɪ ᴠᴇʀɪʀ"),
    BotCommand("hava", "🌦️ ʜᴀᴠᴀ ᴅᴜʀᴜᴍᴜɴᴜ ɢᴏ̈sᴛᴇʀɪʀ"),
    BotCommand("info", "📚 ɢʀᴜᴘ ʙɪʟɢɪʟᴇʀɪɴɪ ᴠᴇʀɪʀ"),
]

async def set_commands(client):
    
    await client.set_bot_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
    
    
    await client.set_bot_commands(group_commands, scope=BotCommandScopeAllGroupChats())

class LostMuzik(Client):
    def __init__(self):
        super().__init__(
            "LostMuzik",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
        )
        LOGGER(__name__).info(f"Bot Başlatılıyor...")

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.mention = get_me.mention
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "» **ʙᴏᴛ ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
            )
        except:
            LOGGER(__name__).error(
                "Bot, günlük grubuna erişemedi. Botunuzu günlük kanalınıza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Lütfen Bot'u Logger Grubunda Yönetici olarak tanıtın")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"{self.name} olarak başlatıldı")
