from pyrogram import Client
from pyrogram.types import CallbackQuery
import logging , os 

class SexoBot():
    def __init__(self):
        self.app = Client(
            "SexoBot",
            api_id    = 24648014,#API ID de Telegram App
            api_hash  = '3575a0f1524c2a08cc297fbd5355e318',#API Hash de Telegram app
            bot_token = '7300108124:AAEPA0JRUCttcyFPIgGDytJu2PeUaUKbi1E',#Token bot Telegram
            plugins   =  dict(root="plugins"))

        @self.app.on_callback_query()
        def clod(client, call: CallbackQuery):
            data = call.data.split(":")

            if call.from_user.id != int(data[1]):return call.answer("Botones bloqueados.")
            else: call.continue_propagation()

    def runn(self):
        os.system("cls")
        logging.basicConfig(level=logging.INFO)
        self.app.run()



SexoBot().runn()


"""
    ____                          ___                         _    __
   / __ \  ___    _  __          /   | _      __  ____ _   (_)  / /_
  / /_/ / / _ \  | |/_/         / /| || | /| / / / __ `/  / /  / __/
 / _, _/ /  __/ _>  <          / ___ || |/ |/ / / /_/ /  / /  / /_
/_/ |_|  \___/ /_/|_|         /_/  |_||__/|__/  \__,_/  /_/   \__/
                                                𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝗔𝗽𝗶𝘀 「🐉」

『⁣✪』User: 6411167257 
『⁣✪』Code by: @RexAwait 👑"""

#Note: Colocar las proxys aunque por defecto andan desactivadas en session.