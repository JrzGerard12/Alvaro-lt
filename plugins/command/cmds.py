from srca.configs import addCommand, Client
from paquetes.plantillas import commd

@addCommand('cmds')
def start(_, m):
    Client.send_photo(
        _,
        chat_id=m.chat.id,
        photo='https://i.ibb.co/ynZ4nVVR/IMG-20250602-033447-327.jpg',
        caption=f"""<b>¡Bienvenido(a), @{m.from_user.username}!</b>

<b>Gracias por usar nuestros servicios. Descubre nuestra amplia gama de herramientas y comandos disponibles. Utiliza los botones a continuación para explorar todas las funcionalidades que ofrecemos.</b>""",
        reply_markup=commd(m.from_user.id)
    )