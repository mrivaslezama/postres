import reflex as rx

from .nav import navbar
from .grid import grid
from .foot import footer

from rxconfig import config

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),

        rx.box(
            child,
            bg="white",
            padding="1em",
            width="100%",
        ),
        grid(),       
        footer(),
        rx.color_mode.button(position="bottom-left", id='my-light-mode-btn'),
        
        id="my-base-container"
    )
