
import reflex as rx

from rxconfig import config

from WebSelenium.pages.Index import index
from WebSelenium.pages.Buscadores import buscadores
from WebSelenium.pages.RedesSociales import redesSociales

class State(rx.State):
    pass

app = rx.App()
app._compile()
