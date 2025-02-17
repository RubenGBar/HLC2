import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Home", height="40px"),
        rx.text("About", height="40px"),
        position = "sticky",
        padding_x = "16px",
        padding_y = "8px",
        bg = "blue",
        z_index = 999,

    )
