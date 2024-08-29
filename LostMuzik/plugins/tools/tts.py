from pyrogram import Client, filters
from gtts import gTTS
from LostMuzik import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
        return

    text = ""

    
    if message.reply_to_message:
        text = message.reply_to_message.text

    
    else:
         
        text_parts = message.text.split(maxsplit=1)
        if len(text_parts) < 2:
            await message.reply("🔊 **Metin sese çevriliyor... Lütfen bekleyin.**")
            return

        text = text_parts[1]

    
    res_message = await message.reply("🔊 **Metin sese çevriliyor... Lütfen bekleyin.**")

    
    await asyncio.sleep(2)

    
    tts = gTTS(text=text, lang='tr')  
    tts.save("output.mp3") 

    
    await client.send_voice(message.chat.id, voice="output.mp3")

    # Geçici dosyayı silme
    os.remove("output.mp3")

    
    await message.delete()
    await res_message.delete()
