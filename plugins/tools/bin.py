import requests
from srca.configs import addCommand

@addCommand('bin')
def bin(_, m):
    bins = m.text.split(' ')

    if len(bins) < 2:
        return m.reply('Ingrese el BIN.')
    if len(bins[1]) < 6:
        return m.reply('BIN incompleto')

    req = requests.get(f'https://bins.antipublic.cc/bins/{bins[1]}')

    if '"detail":"' in req.text:
        return m.reply(req.json()['detail'])

    texto = f'''[🔎] 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐜𝐢𝐨𝐧
{req.json()['country_flag']} 𝗕𝗜𝗡: <code>{bins[1][:6]}</code> 
━━━━━━━━━━━━━━━━━━
[⍟] Info: <code>{req.json()['brand']} - {req.json()['level']}</code>
[⍟] Bank: {req.json()['bank']}
[⍟] Type: {req.json()['type']}
[⍟] Country: {req.json()['country_name']} {req.json()['country_flag']}
━━━━━━━━━━━━━━━━━━
 • <b>Check by: @{m.from_user.username}</b>'''
    m.reply(texto)