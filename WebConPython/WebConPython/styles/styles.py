import reflex as rx
from enum import Enum

# Constantes
MAX_WIDTH = "600px"

# Enumerado Sizes
class Size(Enum):
    SMALL = "8px"
    MEDIUM = "12px"
    DEFAULT = "16px"
    BIG = "32px"

# Styles
BASE_STYLE = {
    rx.button:{
        "width" : "100%",
        "height" : "100%",
    },
    rx.link:{
      "text_decoration" : "none",
    },
    rx.vstack:{
        "width" : "100%",
    }
}

# Sryles for texts
button_title_style = dict(
    font_size= Size.DEFAULT
)

button_body_style = dict(
    font_size= Size.MEDIUM
)