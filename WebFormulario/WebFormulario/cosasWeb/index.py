import reflex as rx

from WebFormulario.cosasWeb.formulario import Formulario

@rx.page(
    route="/", title="Formulario de Registro - Mi web",
)
def Index() -> rx.Component:
    return rx.center(
        rx.vstack(
            Formulario(),
            align="center",
            max_width="600px",
            margin_y="32px",
        )
    )