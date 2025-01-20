import reflex as rx

def feature_item(feature: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "check", color=rx.color("blue", 9), size=21
        ),
        rx.text(feature, size="4", weight="regular"),
    )

def standard_features() -> rx.Component:
    return rx.vstack(
        rx.image(src="/proyectos.jpg",
                    width="100%",
                    height="auto",
                    ),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("250 credits for image generation"),
        feature_item("+30% Extra free credits"),
        feature_item("Credits never expire"),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )

def page_content() -> rx.Component:
    return rx.vstack(
        rx.image(src="/autanamuebles.png",
                    width="15em",
                    height="auto",
                    ),
        rx.text("Pagina web de la empresa Autana Muebles"),
        rx.link("Visita Autana Muebles", href="https://mrivaslezama.github.io/autanas/", target="_blank"),
        
        
        spacing="3",
        width="100%",
        align_items="start",
    )


def card1() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Pagina web",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
       page_content(),
        rx.spacer(),

        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )

def page_content2() -> rx.Component:
    return rx.vstack(
        rx.image(src="/Tiaromy.png",
                    width="15em",
                    height="auto",
                    ),
        rx.text("Pagina web del restaurant La Tia Romy"),
        rx.link("Visita La Tia Romy", href="https://mrivaslezama.github.io/latiaromyrestaurante/", target="_blank"),
        
        
        spacing="3",
        width="100%",
        align_items="start",
    )


def card2() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Pagina web",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
       page_content2(),
        rx.spacer(),

        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Diseños 3D",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        standard_features(),
        rx.spacer(),

        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )

def pricing_card_popular() -> rx.Component:
    return rx.vstack(
      rx.grid(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "$69.99",
                    trim="both",
                    as_="s",
                    size="3",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "$18.99",
                    trim="both",
                    size="6",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            rx.badge(
                "POPULAR",
                size="2",
                radius="full",
                variant="soft",
                color_scheme="blue",
            ),
            align_items="center",
            justify="between",
            height="35px",
            width="100%",
        ),
        rx.text(
            "250 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        popular_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            width="100%",
            color_scheme="blue",
        
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("blue", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
        
      )
   
    )



def pricing_cards() -> rx.Component:
    return rx.hstack(
                rx.flex(
                    card1(),
                    border_radius="20%",
                   
                ),
                rx.flex(
                    card2(),
                    border_radius="20%",
                   
                )
            ),
    
    

    # Making a backup this code worked...abs
import reflex as rx

def grid() -> rx.Component:
    """Creates a grid layout for displaying products."""
    return rx.vstack(
        # Title Section
        rx.text(
            "Helados y postres",
            weight="bold",
            size="9",
            width="100%",
            text_align="center",
            font_family="'Pacifico', cursive",
            color="#99A7FF",
            padding="12px",
        ),
        rx.section(
            rx.center(
                rx.hstack(
                    rx.vstack(
                        rx.heading("Smoothies y batidos"),
                        rx.text("Helado tradicional de diferentes Sabores: "), 
                        rx.text("Parchita, chocolate, tres-leches, coco, durazno, frutilla, melon, vainilla..."),
                        padding="12px",
                        color="#99A7FF",
                        
                ),
                rx.image(src="/smoothie1.jpg", width="400px", height="auto"),
            ) 
        ),
        background_color="pink",
        justify="center",  # Center the section horizontally
        align_items="center",  # Center the section vertically 
        width="100%",  # Ensure the section spans the full width
        ),
        rx.section(
            rx.center(
                rx.hstack(
                    rx.vstack(
                        rx.heading("Helado (Tetas).."),
                        rx.text("Helado tradicional de diferentes Sabores: "), 
                        rx.text("Parchita, chocolate, tres-leches, coco, durazno, frutilla, melon, vainilla..."),
                        padding="12px",
                        color="#99A7FF",
                        
                ),
                rx.image(src="/parch.png", width="200px", height="auto"),
            ) 
        ),
        ),
        background_color="pink",
        justify="center",  # Center the section horizontally
        align_items="center",  # Center the section vertically 
        width="100%",  # Ensure the section spans the full width
    )
