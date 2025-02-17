import reflex as rx

from WebConPython.Views.Footer.footer import footer
from WebConPython.Views.Header.header import header
from WebConPython.Views.Links.links import links
from WebConPython.Views.NavBar.navbar import navbar
from WebConPython.styles.styles import *
from WebConPython.routes import *

@rx.page(
    route=Ruta.INDEX.value,
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
        header(),
                links(),
                align="center",
                max_width=MAX_WIDTH,
                margin_y=Size.BIG,
            ),
        ),
        footer(),
    )