import reflex as rx

def listaEnlacesFavoritos():
    return rx.list(
        rx.list.item(
            rx.link("Buscadores", href="/Buscadores", id="enlaceBuscadores"),
        ),
        rx.list.item(
            rx.link("Redes Sociales", href="/Redes_Sociales", id="enlaceRedesSociales"),
        ),
        id="listaEnlaces",
    )

def listaEnlacesBuscadores():
    return rx.list(
        rx.list.item(
            rx.link("Google", href="https://www.google.com/", is_external= True, id="enlaceGoogle"),
        ),
        rx.list.item(
            rx.link("Bing", href="https://www.bing.com/", is_external= True, id="enlaceBing"),
        ),
        rx.list.item(
            rx.link("Baidu", href="https://www.baidu.com/", is_external= True, id="enlaceBaidu"),
        ),
        id="listaEnlacesBuscadores",
    )

def listaEnlacesRedesSociales():
    return rx.list(
        rx.list.item(
            rx.link("Instagram", href="https://www.instagram.com/", is_external= True, id="enlaceInstagram"),
        ),
        rx.list.item(
            rx.link("Tik Tok", href="https://www.tiktok.com/", is_external= True, id="enlaceTikTok"),
        ),
        rx.list.item(
            rx.link("Facebook", href="https://www.facebook.com/", is_external= True, id="enlaceFacebook"),
        ),
        id="listaEnlacesRedesSociales",
    )