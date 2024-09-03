import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            "LostMuzikString1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            "LostMuzikString2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            "LostMuzikString3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            "LostMuzikString4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            "LostMuzikString5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Asistanlar Başlatılıyor")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Eskiyalar")
                await self.one.join_chat("Eskiyalar")
                await self.one.join_chat("Eskiyalar")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "» **ᴀsɪsᴛᴀɴ 𝟷 ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
                )
            except:
                LOGGER(__name__).error(
                    f"Asistan Hesabı 1, Log grubuna erişemedi. Asistanınızın log grubunda olduğundan ve yönetici olduğundan emin olun!"
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Asistan 1 Başlatıldı: {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("Eskiyalar")
                await self.two.join_chat("Eskiyalar")
                await self.two.join_chat("Eskiyalar")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "» **ᴀsɪsᴛᴀɴ 𝟸 ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
                )
            except:
                LOGGER(__name__).error(
                    f"Asistan Hesabı 2, Log grubuna erişemedi. Asistanınızın log grubunda olduğundan ve yönetici olduğundan emin olun!"
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"Asistan 2 Başlatıldı: {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("Eskiyalar")
                await self.three.join_chat("Eskiyalar")
                await self.three.join_chat("Eskiyalar")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, "» **ᴀsɪsᴛᴀɴ 𝟹 ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
                )
            except:
                LOGGER(__name__).error(
                    f"Asistan Hesabı 3, Log grubuna erişemedi. Asistanınızın log grubunda olduğundan ve yönetici olduğundan emin olun!"
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(
                f"Asistan 3 Başlatıldı: {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("Eskiyalar")
                await self.four.join_chat("Eskiyalar")
                await self.four.join_chat("Eskiyalar")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, "» **ᴀsɪsᴛᴀɴ 𝟺 ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
                )
            except:
                LOGGER(__name__).error(
                    f"Asistan Hesabı 4, Log grubuna erişemedi. Asistanınızın log grubunda olduğundan ve yönetici olduğundan emin olun!"
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(
                f"Asistan 4 Başlatıldı: {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("Eskiyalar")
                await self.five.join_chat("Eskiyalar")
                await self.five.join_chat("Eskiyalar")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, "» **ᴀsɪsᴛᴀɴ 𝟻 ʙᴀşᴀʀıʟı ʙɪʀ şᴇᴋɪʟᴅᴇ ʙᴀşʟᴀᴛıʟᴅı**"
                )
            except:
                LOGGER(__name__).error(
                    f"Asistan Hesabı 5, Log grubuna erişemedi. Asistanınızın log grubunda olduğundan ve yönetici olduğundan emin olun!"
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(
                f"Asistan 5 Başlatıldı: {self.five.name}"
            )
