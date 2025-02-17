import reflex as rx

from WebSelenium.Routes import Routes
from WebSelenium.views.Headers.Header import headerIndex
from WebSelenium.views.Listas.List import listaEnlacesFavoritos


@rx.page(
    route=Routes.INDEX.value,
)
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            headerIndex(),
            listaEnlacesFavoritos(),
            align="center",
            max_width= "600px",
            margin_y= "32px",
        )
    )
