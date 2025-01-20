import reflex as rx

def multi() -> rx.Component:
    return rx.flex(
            rx.flex(
                rx.box(
                    rx.text("Mouredev", size="7"),
                        rx.link(
                            rx.text("https://www.youtube.com/watch?v=2u7JlBEavx0&t=2158s", size="2"),
                            on_click=rx.redirect("https://www.youtube.com/watch?v=2u7JlBEavx0&t=2158s",  external=True,)
                        ),

                    bg=rx.color("accent", 3),
                    width=["100%", "100%", "50%"],
                    height="100%",
                     text_align="center",
                    padding="2em"
                ),
                rx.box(
                    rx.html(
                        "<img src='https://reflex.dev/reflex_banner.png' />"
                     ),
                    rx.text("Esto sera un titulo", size="7"),
                    rx.link(
                        rx.text("https://www.youtube.com/watch?v=ITOZkzjtjUA", size="2"),
                        on_click=rx.redirect("https://www.youtube.com/watch?v=ITOZkzjtjUA",  external=True,)
                    ),
                    bg=rx.color("accent", 5),
                    width=["100%", "100%", "50%"],
                    height="100%",
                    text_align="center",
                    padding="2em"
                ),
                width="100%",
                height="100%",
                spacing="4",
                flex_direction=["column", "column", "row"],
            ),
            rx.box(
                bg=rx.color("accent", 7), width="100%", height="50%"
            ),
            rx.box(
                bg=rx.color("accent", 9), width="100%", height="50%"
            ),
            bg=rx.color("accent", 10),
            spacing="4",
            padding="1em",
            flex_direction="column",
            height="600px",
            width="100%",
        )


        