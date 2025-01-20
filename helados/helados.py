"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from rxconfig import config
from .ui.multi import multi
from .ui.contact import contact_form
from .ui.toast import try_some_toast
from .ui.avatar import avatar
from .ui.base import base_page
from .ui.grid import grid

class State(rx.State):
    """The app state."""
    label = "Bienvenidos!"
    
    def scroll_to_productos(self):
        return rx.call_script("document.getElementById('productos').scrollIntoView({behavior: 'smooth'})")
    
def index() -> rx.Component:
    # Hero Section
    hero = rx.box(
        rx.vstack(
            rx.heading(
                "!Helados, smothies y postres!",
                size="9",
                color="#FFFFFF",
                font_weight="bold",
                text_shadow="3px 3px 8px rgba(0,0,0,0.6)",
                text_align="center",
                padding_x="1em",
                font_family="'Pacifico', cursive",
                letter_spacing="0.02em",
            ),
            rx.text(
                "Delicias artesanales",
                size="7",
                color="#FFFFFF",
                text_align="center",
                text_shadow="2px 2px 6px rgba(0,0,0,0.6)",
                padding_x="1em",
                max_width="800px",
                font_family="'Quicksand', sans-serif",
                font_weight="medium",
            ),
            
            spacing="6",
            align="center",
            justify="center",
            height="100%",
            max_width="1200px",
            margin="0 auto",
            padding_x="1em",
        ),
        width="100%",
        height="100vh",
        background_image="url('/hero-icecream.jpg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        position="relative",
        display="flex-grow",
        align_items="center",
        justify_content="center",
        _before={
            "content": "''",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "background": "linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.4))",
            "z_index": "0",
        },
        sx={
            "& > *": {
                "position": "relative",
                "z_index": "2",
            }
        },
    )
   
       
    # Main Container
    return base_page(
        rx.vstack(
            hero,
                  
            spacing="0",
            width="100%",
            align="stretch",
        )
    )

    

   
app = rx.App()
app.add_page(index)
