#
# Copyright (C) 2021-2023 by LostBots@Github, < https://github.com/LostBots >.
#
# This file is part of < https://github.com/LostBots/LostMuzik > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LostBots/LostMuzik/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LostMuzik import LOGGER, app, userbot
from LostMuzik.core.call import LostMuzik
from LostMuzik.plugins import ALL_MODULES
from LostMuzik.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LostMuzik").error(
            "Tanımlanmış Asistan İstemcisi Yok!.. İşlemden Çıkılıyor."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LostMuzik").warning(
            "Tanımlanmış Spotify Vars'ı yok. Botunuz Spotify sorgularını oynatamayacak."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LostMuzik.plugins" + all_module)
    LOGGER("LostMuzik.plugins").info(
        "Başarıyla İçe Aktarılan Modüller"
    )
    await userbot.start()
    await LostMuzik.start()
    try:
        await LostMuzik.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("LostMuzik").error(
            "[HATA] - \n\Lütfen Log Grubunuzun Sesli Aramasını Açın. Log grubunuzda sesli aramayı asla kapatmadığınızdan sonlandırmadığınızdan emin olun."
        )
        sys.exit()
    except:
        pass
    await LostMuzik.decorators()
    LOGGER("LostMuzik").info("Lost Muzik Botu Başarıyla Başladı")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LostMuzik").info("Lost Muzik Botu Durdu")
