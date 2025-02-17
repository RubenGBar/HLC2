import reflex as rx

from WebConPython.styles.styles import *
from WebConPython.pages.index import index
from WebConPython.pages.courses import courses

class State(rx.State):
    pass

app = rx.App(style=BASE_STYLE)
#app.add_page(index)
app._compile()