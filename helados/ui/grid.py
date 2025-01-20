import reflex as rx

def grid():
  """A Reflex component for displaying a product grid layout."""

  title_section = rx.text(
      "Helados y postres",
      weight="bold",
      size="9",
      width="100%",
      text_align="center",
      font_family="'Pacifico', cursive",
      color="#99A7FF",
      padding="12px",
  )

  smoothies_section = rx.section(
      rx.center(
          rx.hstack(
              rx.vstack(
                  rx.heading("Smoothies y batidos"),
                  rx.text("Saludable y deliciososaludable y delicioso, sabores: "),
                  rx.text("Chocolate, tres-leches, coco, durazno, frutilla, melon, ..."),
                  padding="12px",
                  color="#FFB6C1",
              ),
              rx.image(src="/smoothie1.jpg", width="10em", height="auto"),
          )
      ),
      background_color="#E0FFFF",  # Light Cyan
      width="100%",  # Make the section full width
  )

  panes_section = rx.section(
      rx.center(
          rx.hstack(
              rx.vstack(
                  rx.heading("Panes y cakes"),
                  rx.text("Panes y pasteles a pedido "),
                  rx.text("Chocolate, tres-leches, piña, red-velvet"),
                  padding="20px",
                  color="#99A7FF",
              ),
              rx.image(src="/panes.jpeg", width="200px", height="auto"),
          )
      ),
      background_color="white",  # Light Pink
        width="100%",  # Make the section full width
  )

  postres_section = rx.section(
      rx.center(
          rx.hstack(
              rx.vstack(
                  rx.heading("Postres a pedido"),
                  rx.text("Deliciosos postres, cakes para toda ocasión, sabores: "),
                  rx.text("Chocolate, cheesecakes, cakes..."),
                  
                  color="#FFB6C1",
              ),
              rx.image(src="/chocolate-icecream.jpg", width="200px", height="auto"),
          )
      ),
      background_color="#E0FFFF",  # Light Cyan
      width="100%",  # Make the section full width
  )

  crepes_section = rx.section(
      rx.center(
          rx.hstack(
              rx.vstack(
                  rx.heading("Crepes y pancakes"),
                  rx.text("Panes y pasteles a pedido "),
                  rx.text("Chocolate, tres-leches, piña, red-velvet"),
                  padding="20px",
                  color="#99A7FF",
              ),
              rx.image(src="/panes.jpeg", width="200px", height="auto"),
          )
      ),
      background_color="white",  # Light Pink
        width="100%",  # Make the section full width
  )



  ice_cream_section = rx.section(
      rx.center(
          rx.hstack(
              rx.vstack(
                  rx.heading("Helado (Tetas)..."),
                  rx.text("Helado tradicional de diferentes Sabores: "),
                  rx.text("Parchita, chocolate, tres-leches, coco, durazno, frutilla, melon, vainilla..."),
                  padding="20px",
                  color="#99A7FF",
              ),
              rx.image(src="/parch.png", width="200px", height="auto"),
          )
      ),
      background_color="#FFB6C1",  # Light Pink
        width="100%",  # Make the section full width
  )

  return rx.vstack(
      title_section,
      smoothies_section,
      panes_section,
      postres_section,
      crepes_section,
      ice_cream_section,
      justify="center",  # Center the section horizontally
      align_items="center",  # Center the section vertically
      width="100%",
      background_color="white",  # Light Pink
  )