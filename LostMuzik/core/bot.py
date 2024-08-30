import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

import config

from ..logging import LOGGER


private_commands = [
    BotCommand("start", "🎧 Botu başlatır"),
    BotCommand("yardim", "📖 Yardım menüsünü gösterir"),
]


group_commands = [
    BotCommand("oynat", "🔼 Müziği oynatır"),
    BotCommand("voynat", "📹 Videoyu oynatır"),
    BotCommand("atla", "⏭️ Sonraki Parçaya Geçer"),
    BotCommand("duraklat", "⏸️ Çalan Parçayı Durdurur"),
    BotCommand("devam", "▶️ Çalan Parçayı Devam Ettirir"),
    BotCommand("son", "⏹️ Çalan Parçayı Kapatır"),
    BotCommand("karistir", "🔀 Çalan Parçayı Karıştırır"),
    BotCommand("dongu", "🔄 Çalan Parçayı Tekrarlar"),
    BotCommand("sira", "📖 Çalma Listelerini Gösterir"),
    BotCommand("ilerisar", "⏩ Parçayı İleri Sarar"),
    BotCommand("gerisar", "⏪ Parçayı Geri Sarar"),
    BotCommand("playlist", "📖 Çalma Listenizi Gösterir"),
    BotCommand("bul", "📩 Seçtiğiniz Parçayı İndirir"),
    BotCommand("ayarlar", "⚙️ Bot Ayarlarını Gösterir"),
    BotCommand("restart", "🔃 Botu Yeniden Başlatır"),
    BotCommand("id", "🆔 Kullanıcı ID'sini Verir"),
    BotCommand("hava", "🌦️ Hava Durumunu Gösterir"),
    BotCommand("reload", "❤️‍🔥 Yönetici Önbelleğini Günceller"),
    
]

async def set_commands(client):
    
    await client.set_bot_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
    
    
    await client.set_bot_commands(group_commands, scope=BotCommandScopeAllGroupChats())

class AlexaBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
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
                config.LOG_GROUP_ID, "» **Bot Başarılı Bir Şekilde Başlatıldı** 🔮"
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
