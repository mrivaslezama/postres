import reflex as rx

def footer_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        color="#FFD6E0",
        _hover={"color": "#A5D8FF"},
        text_decoration="none",
        font_size="1rem",
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.icon(
            icon,
            color="#FFD6E0",
            font_size="1.5em",
            _hover={"color": "#A5D8FF"},
        ),
        href=href,
        text_decoration="none",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(border_color="#333333"),
            rx.grid(
                
                
                # Quick Links
                rx.vstack(
                    rx.heading("Enlaces", size="4", color="#FFFFFF", text_align="center", margin_top="1em"),
                    rx.hstack(
                        footer_link("Inicio", "/"),
                        footer_link("productos", "#productos"),
                        footer_link("nosotros", "/nosotros"),
                        footer_link("contacto", "/contacto"),
                        spacing="2",
                        align_items="center",
                    ),
                    align_items="center",
                    width="100%",
                ),
                
                # Social Media
                rx.vstack(
                    rx.heading("Síguenos", size="4", color="#FFFFFF", text_align="center", margin_top="1em"),
                    rx.hstack(
                        social_link("instagram", "https://instagram.com"),
                        social_link("facebook", "https://facebook.com"),
                        social_link("twitter", "https://twitter.com"),
                        spacing="4",
                        justify_content="center",
                    ),
                    align_items="center",
                    width="100%",
                ),
                
                template_columns="repeat(3, 1fr)",
                gap="6",
                padding_y="6",
                justify_items="center",
                align_items="start",
                width="100%",
            ),
            
            rx.divider(border_color="#333333"),
            rx.text(
                "© 2024 Helados Artesanales. Todos los derechos reservados.",
                font_size="0.875rem",
                color="#FFFFFF",
                padding_y="4",
                text_align="center",
            ),
            width="100%",
            spacing="4",
            align_items="center",
        ),
        width="100%",
        background="#111111", 
        padding_x="20rem",
        max_width="1400px",
        margin="0 auto",
    )

