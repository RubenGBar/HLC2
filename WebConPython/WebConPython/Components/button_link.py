import reflex as rx

from WebConPython.styles.styles import button_title_style, button_body_style


def button_link(texto1, url) -> rx.Component:
    return rx.button(
        rx.link(
            rx.text(texto1, style=button_title_style),
            href=url,
            is_external=True,
            color_scheme="mint",
            margin = 10
        ),
        color_scheme="tomato",
    )