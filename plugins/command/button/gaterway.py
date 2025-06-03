from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>あ » Tools 🐉

↯ » Status    » Free
↯ » Type    » <i>Stripe Auth</i>
↯ » Cmmd    » $au
↯ » Format   » <code>$au cc|mm|yy|cvc</code>
━━
↯ » Status    » Free
↯ » Type    » <i>Paypal</i>
↯ » Cmmd    » $pp
↯ » Format   » <code>$pp cc|mm|yy|cvc</code>
━━
↯ » Status    » Free
↯ » Type    » <i>Braintree Auth Avs</i>
↯ » Cmmd    » $chk
↯ » Format   » <code>$chk cc|mm|yy|cvc</code>
━━
↯ » Status    » Free
↯ » Type    » <i>Autorize.Net Charged $5.00</i>
↯ » Cmmd    » $ac
↯ » Format   » <code>$ac cc|mm|yy|cvc</code> 
━━
↯ » Status    » Free
↯ » Type    » <i>APayeezy Charged $50.00</i>
↯ » Cmmd    » $pz
↯ » Format   » <code>$pz cc|mm|yy|cvc</code> 
                        
━━━━━━━━━━━</b>''',reply_markup=atras(message.from_user.id))