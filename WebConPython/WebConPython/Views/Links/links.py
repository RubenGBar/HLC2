import reflex as rx

from WebConPython.Components.button_link import button_link

def links() -> rx.Component:
    return rx.vstack(

        button_link("IESNervion","https://www.institutonervion.es/"),
        button_link("YouTube", "https://www.youtube.com/"),
        button_link("Twitch", "https://www.twitch.tv/"),
        align="center",
    )