import datetime
import reflex as rx

from WebConPython.styles.styles import MAX_WIDTH


def footer()-> rx.Component:
    return rx.center(rx.hstack(
        rx.icon("hand-metal"),
        rx.text(datetime.date.today().year),
        rx.link("PÁGINA DE RUBÉN GARCÍA", href="http://localhost:3000/"),
        align="center",
        max_width=MAX_WIDTH,

    ))