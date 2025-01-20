import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            size="3",
            weight="medium",
            color="#4A5568",
            _hover={"color": "#A5D8FF"},
            transition="all 0.3s ease-in-out"
        ),
        href=url,
        padding="1",
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/0.png",
                        width="2rem",
                        height="auto",
                        margin="0.5em",
                    ),
                    rx.heading(
                        "Postres & Helados Artesanales",
                        size="2",
                        color="#4A5568",
                        font_family="'Dancing Script', cursive",
                    ),
                    align_items="center",
                ),
               
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("productos", "#productos"),
                    navbar_link("nosotros", "/nosotros"),
                    navbar_link("contactanos", "/contactanos"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/0.png",
                        width="3.5rem",
                        height="auto",
                        margin="0.5em",
                    ),
                    rx.heading(
                        "Postres & Helados Artesanales",
                        size="4",
                        color="#4A5568",
                        font_family="cursive",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("menu", size=24),
                            variant="ghost",
                            color="pink.800",
                            _hover={"bg": "pink.50"}
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            rx.link("Inicio", href="/", width="100%", text_decoration="none"),
                            color="pink.900",
                        ),
                        rx.menu.item(
                            rx.link("nosotros", href="/nosotros", width="100%", text_decoration="none"),
                            color="pink.900",
                        ),
                        rx.menu.item(
                            rx.link("contactanos", href="/contactanos", width="100%", text_decoration="none"),
                            color="pink.900",
                        ),
                        rx.menu.separator(),
                        rx.menu.item(
                            rx.hstack(
                                rx.icon("log-in"),
                                rx.text("Iniciar Sesión"),
                                width="100%",
                            ),
                            color="pink.900",
                        ),
                        padding="1em",
                        background_color="white",
                        border_radius="0.5em",
                        box_shadow="0px 5px 15px rgba(0,0,0,0.1)",
                    ),
                    transition="all 0.2s",
                ),
                justify="between",
                align_items="center",
                id="my-nav-hstack-desktop",
            ),
        ),
        background="linear-gradient(to right, #FFD6E0, #FFF5E1)",
        backdrop_filter="blur(8px)",
        border_bottom="1px solid",
        border_color="rgba(255, 214, 224, 0.3)",
        padding="0.5em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id="my-main-nav",
    )