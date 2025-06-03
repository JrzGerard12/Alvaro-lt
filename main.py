from pyrogram import Client
from pyrogram.types import CallbackQuery
import logging , os 

class PepitoBot():
    def __init__(self):
        self.app = Client(
            "PepitoBot",
            api_id    = 28463065 ,
            api_hash  = '9fe32a7769cbee12d7b2f49a9fea22a0',
            bot_token = '7666317498:AAG4Km53zPkggVSB_BbwFc0ZctBe-xMoAMM',
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


if __name__ == "__main__":
    PepitoBot().runn()
    """