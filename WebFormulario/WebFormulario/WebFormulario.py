"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from WebFormulario.cosasWeb.index import Index

class State(rx.State):
    pass

app = rx.App()
app._compile()
