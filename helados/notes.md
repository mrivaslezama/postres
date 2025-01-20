

# min 33:03 Build Full Stack Web Apps in Pure Python with Reflex
# min37:12 - hi putted before base_page function - it seems to work fine here as well... 
# 39:29 using navbar recipe
# Better code management --43:49
# Identifying rendered components in the browser --46:40

# Full width navbar and content


rx.box(
    rx.container(
        rx.card(
            "This content is constrained to a max width of 448px.",
            width="100%",
        ),
        size="1",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 688px.",
            width="100%",
        ),
        size="2",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 880px.",
            width="100%",
        ),
        size="3",
    ),
    background_color="var(--gray-3)",
    width="100%",
)