from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>あ » Tools 🐉

↯ » Type    » <i>Braintree </i>
↯ » Cmmd    » $bt
↯ » Format   » <code>$bt cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintree Charged $1</i>
↯ » Cmmd    » $b3
↯ » Format   » <code>$b3 cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintree ccn Avs</i>
↯ » Cmmd    » $chk
↯ » Format   » <code>$chk cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintee Masive Checking</i>
↯ » Cmmd    » $mass
↯ » Format   » <code>$mass cc|mm|yy|cvc</code>                          
━━━━━━━━━━━</b>''',reply_markup=atras(message.from_user.id))