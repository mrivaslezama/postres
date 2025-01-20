import reflex as rx

def try_some_toast():
    return rx.fragment(
        rx.button("🥂", on_click=rx._x.toast.info("Cheers"), variant="outline"),
        rx._x.toast.provider(),
    )