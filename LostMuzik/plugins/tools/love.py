from pyrogram import Client, filters
import random
from LostMuzik import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "**Aşk kokusu havada ama biraz kıvılcıma ihtiyacı var.**",
            "**İyi bir başlangıç.**",
            "Bu sadece güzel aşkın başlangıcı.**"
        ])
    elif love_percentage <= 70:
        return random.choice([
            "**Aranızda güçlü bir bağ var. Onu güçlendirin.***",
            "**İyi bir şansın var. Üzerinde çalış.**",
            "**Aşk çiçek açıyor, devam et.**"
        ])
    else:
        return random.choice([
            "**Vay! Sizi tebrik ederim evlenmeniz gerek!**",
            "**Mükemmel aşk! Bu bağa değer verin.**",
            "**Birlikte olmaya mahkumuz. Tebrikler!**"
        ])
        
@app.on_message(filters.command("ship", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"**{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}**"
    else:
        response = "Lütfen /ship komutundan sonra iki isim girin."
    app.send_message(message.chat.id, response)
