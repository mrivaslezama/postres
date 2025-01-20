import reflex as rx

def avatar() -> rx.Component:
    return rx.image(
        src="/helatetas.png",
        width="400px",
        height="400px",
        border_radius="50%",
        margin_bottom="8px",
    )

       