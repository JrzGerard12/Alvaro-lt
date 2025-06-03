from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("perfi"))
def perfil_cmon(client, m):
    try:
        perfil_text = '''<b>あ » Perfil

↯ » ID: <code>{}</code>
↯ » Username: @{}
↯ » Rango: Owner

━━━━━━━━━━━━━━━</b>'''
        m.edit_message_text(
            perfil_text.format(m.from_user.id, m.from_user.username),
            reply_markup=atras(m.from_user.id)
        )
    except:
        pass