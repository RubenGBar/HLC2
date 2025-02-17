import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

def Formulario() -> rx.Component:
    return rx.vstack(
        rx.text("Formulario de Registro", align="center", size="7", weight="bold", id="Cabecera"),
        rx.form(
            rx.hstack(
                rx.text("Nombre:", id="nombreTexto"),
                rx.input(
                    id="nombreInput",
                    name="nombre",
                    type="text",
                    max_length=50
                ),
            ),
            rx.hstack(
                rx.hstack("Apellido:", id="apellidoTexto"),
                rx.input(
                    id="apellidoInput",
                    name="apellido",
                    type="text",
                    max_length=50
                )
            ),
            rx.hstack(
                rx.text("Sexo:", id="sexoTexto"),
                rx.radio(
                    ["Hombre", "Mujer"],
                    name="sexo",
                    direction="column",
                    id="sexoRadio"
                ),
            ),
            rx.hstack(
                rx.text("Correo:", id="correoTexto"),
                rx.input(
                    id="correoInput",
                    type="text",
                    name="correo",
                ),
            ),
            rx.vstack(
                rx.checkbox(
                    text="Deseo recibir información sobre novedades y ofertas",
                    id="checkNovedades",
                    name="novedades",
                    default_checked=True,
                ),
                rx.checkbox(
                    text="Declaro haber leído y aceptar las condiciones generales del programa y la normativa sobre protección de datos.",
                    name="condiciones",
                    id="checkCondiciones",
                    default_checked=False,
                ),
                rx.button(
                    "Enviar",
                    type="submit",
                    id="botonEnviar"
                ),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
            id="formulario",
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )