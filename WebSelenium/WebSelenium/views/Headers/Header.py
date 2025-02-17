import reflex as rx

def headerIndex():
    return rx.hstack(
        rx.heading("Enlaces Favoritos", id="Cabecera")
    )

def headerBuscadores():
    return rx.hstack(
        rx.heading("Buscadores", id="Cabecera")
    )

def headerRedesSociales():
    return rx.hstack(
        rx.heading("Redes Sociales", id="Cabecera")
    )
