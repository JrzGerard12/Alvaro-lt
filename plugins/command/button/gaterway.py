from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>あ » Tools 🐉

↯ » Type    » <i>Stripe Auth</i>
↯ » Cmmd    » $au
↯ » Format   » <code>$au cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintree Charged $1</i>
↯ » Cmmd    » $b3
↯ » Format   » <code>$pp cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintree ccn Avs</i>
↯ » Cmmd    » $chk
↯ » Format   » <code>$chk cc|mm|yy|cvc</code>
━━
↯ » Type    » <i>Braintee Masive Checking</i>
↯ » Cmmd    » $mass
↯ » Format   » <code>$pf cc|mm|yy|cvc</code> 
━━
↯ » Type    » <i>Ubdate</i>
↯ » Cmmd    » $
↯ » Format   » <code>$ cc|mm|yy|cvc</code>                         
━━━━━━━━━━━</b>''',reply_markup=atras(message.from_user.id))