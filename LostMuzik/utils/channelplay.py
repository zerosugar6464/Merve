#
# Copyright (C) 2021-2023 by LostBots@Github, < https://github.com/LostBots >.
#
# This file is part of < https://github.com/LostBots/LostMuzik > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LostBots/LostMuzik/blob/master/LICENSE >
#
# All rights reserved.
#

from LostMuzik import app
from LostMuzik.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(
                    _["setting_12"], show_alert=True
                )
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(
                    _["cplay_4"], show_alert=True
                )
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel
