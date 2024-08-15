#
# Copyright (C) 2021-2023 by LostBots@Github, < https://github.com/LostBots >.
#
# This file is part of < https://github.com/LostBots/LostMuzik > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LostBots/LostMuzik/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Yayını Duraklat",
            description=f"Sesli sohbette oynatılan parçayı duraklat.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Yayını Devam Ettir",
            description=f"Sesli sohbette devam eden yayına devam edin.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Yayının Sesini Kapat",
            description=f"Sesli sohbette devam eden yayının sesini kapatın.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Yayının Sesini Aç",
            description=f"Sesli sohbette devam eden yayının sesini açın.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Yayını Atla",
            description=f"Sonraki parçaya geçin. | Belirli parça numarası için: /skip [number] ",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Yayını Sonlandır",
            description="Sesli sohbette devam eden oynatmayı durdurun.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Yayını Karıştır",
            description="Sıraya alınmış parçalar listesini karıştırın.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Yayın Ara",
            description="Belirli bir süreye kadar devam eden akışı arayın.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Döngü Akışı",
            description="Geçerli çalan müziği döngüye alın. | Kullanım: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
