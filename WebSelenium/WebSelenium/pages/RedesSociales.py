import reflex as rx

from WebSelenium.Routes import Routes
from WebSelenium.views.Headers.Header import headerRedesSociales
from WebSelenium.views.Listas.List import listaEnlacesRedesSociales


@rx.page(
    route=Routes.REDES_SOCIALES.value,
)
def redesSociales() -> rx.Component:
    return rx.center(
        rx.vstack(
            headerRedesSociales(),
            listaEnlacesRedesSociales(),
            align="center",
            max_width= "600px",
            margin_y= "32px",
        )
    )
