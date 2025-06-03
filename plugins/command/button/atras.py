from pyrogram import Client, filters
from paquetes.plantillas import commd

@Client.on_callback_query(filters.regex("atras"))
def atras(client, m):
    m.edit_message_text(
        f"""<b>¡Bienvenido(a), @{m.from_user.username}!</b>

<b>Gracias por usar nuestros servicios. Descubre nuestra amplia gama de herramientas y comandos disponibles.</b>""",
        reply_markup=commd(m.from_user.id)
    )