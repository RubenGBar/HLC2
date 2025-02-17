import reflex as rx

from WebSelenium.Routes import Routes
from WebSelenium.views.Headers.Header import headerBuscadores
from WebSelenium.views.Listas.List import listaEnlacesBuscadores


@rx.page(
    route=Routes.BUSCADORES.value,
)
def buscadores() -> rx.Component:
    return rx.center(
        rx.vstack(
            headerBuscadores(),
            listaEnlacesBuscadores(),
            align="center",
            max_width= "600px",
            margin_y= "32px",
        )
    )
