from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("tools"))
def tool_com(client, m):
    m.edit_message_text('''<b>あ » Tools 🐉

━━
↯ » Cmmd    » $bin
↯ » Format   » $bin 456789
━━ 
                        
━━━━━━━━━━━</b>''',reply_markup=atras(m.from_user.id))
