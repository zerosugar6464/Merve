

from config import LOG, LOG_GROUP_ID
import psutil
import time
from LostMuzik import app
from LostMuzik.utils.database import is_on_off
from LostMuzik.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from LostMuzik.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)



async def play_logs(message, streamtype):
    chat_id = message.chat.id
    sayı = await app.get_chat_members_count(chat_id)
    toplamgrup = len(await get_served_chats())
    aktifseslisayısı = len(await get_active_chats())
    aktifvideosayısı = len(await get_active_video_chats())
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"


    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ɢɪᴢʟɪ ɢʀᴜᴘ 🔏"
        logger_text = f"""


**ɢʀᴜᴘ ᴀᴅı:** {message.chat.title} [`{message.chat.id}`]
**ᴜ̈ʏᴇ sᴀʏısı: {sayı}**
**ᴋᴜʟʟᴀɴıᴄı:** {message.from_user.mention}
**ᴋᴜʟʟᴀɴıᴄı ᴀᴅı:** @{message.from_user.username}
**ᴋᴜʟʟᴀɴıᴄı ɪᴅ:** `{message.from_user.id}`
**ɢʀᴜᴘ ʟɪɴᴋɪ:** {chatusername}
**sᴏʀɢᴜ:** {message.text}

**ɪşʟᴇᴍᴄɪ:** {CPU}  ♨️  **ʙᴇʟʟᴇᴋ:** {RAM}  📂  **ᴅᴇᴘᴏʟᴀᴍᴀ:** {DISK}

**ᴛᴏᴘʟᴀᴍ ɢʀᴜᴘ sᴀʏısı: » {toplamgrup}** 

**ᴀᴋᴛɪғ sᴇsʟɪ: {aktifseslisayısı}  🌬️  ᴀᴋᴛɪғ ᴠɪᴅᴇᴏ: {aktifvideosayısı}**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
                await app.set_chat_title(LOG_GROUP_ID, f"ᴀᴋᴛɪғ sᴇsʟɪ - {aktifseslisayısı}")
            except:
                pass
        return
