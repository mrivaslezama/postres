

import reflex as rx


# Crear un componente de texto con diferentes tipos y tamaños de letra
class TextComponent(rx.Component):
    def render(self):
        return rx.View(
            rx.Text("Título Grande", font_size=30, font_weight="bold"),
            rx.Text("Subtítulo", font_size=24, font_style="italic"),
            rx.Text("Texto normal", font_size=16),
            rx.Text("Texto pequeño", font_size=12)
        )

# Crear un componente con diferentes fondos
class BackgroundComponent(rx.Component):
    def render(self):
        return rx.View(
            rx.View("Fondo rojo", background_color="red", padding=10, margin=10),
            rx.View("Fondo azul", background_color="blue", padding=10, margin=10),
            rx.View("Fondo verde", background_color="green", padding=10, margin=10)
        )

# Crear un componente para mostrar fotos
class PhotoComponent(rx.Component):
    def render(self):
        return rx.View(
            rx.Image(src="https://via.placeholder.com/150", alt="Foto 1", width=150, height=150),
            rx.Image(src="https://via.placeholder.com/200", alt="Foto 2", width=200, height=200),
            rx.Image(src="https://via.placeholder.com/250", alt="Foto 3", width=250, height=250)
        )

# Crear un componente principal que combine los anteriores
class MainComponent(rx.Component):
    def render(self):
        return rx.View(
            TextComponent(),
            BackgroundComponent(),
            PhotoComponent()
        )



# 2

import reflex as rx

# Crear un componente de producto individual
class ProductComponent(rx.Component):
    def __init__(self, image_url, name, description, price):
        # Atributos del producto
        self.image_url = image_url
        self.name = name
        self.description = description
        self.price = price

    def render(self):
        return rx.View(
            # Mostrar la imagen del producto
            rx.Image(src=self.image_url, alt=self.name, width=150, height=150),
            # Mostrar el nombre del producto
            rx.Text(self.name, font_size=20, font_weight="bold"),
            # Mostrar la descripción del producto
            rx.Text(self.description, font_size=16),
            # Mostrar el precio del producto
            rx.Text(f"${self.price}", font_size=18, color="green"),
            padding=10,
            margin=10,
            border="1px solid #ddd",
            border_radius=5,
            box_shadow="2px 2px 5px rgba(0,0,0,0.1)"
        )

# Crear un componente de sección de productos
class ProductSection(rx.Component):
    def __init__(self, products):
        # Lista de productos
        self.products = products

    def render(self):
        # Renderizar una vista con todos los productos
        return rx.View(
            *[ProductComponent(**product).render() for product in self.products],
            display="flex",
            flex_wrap="wrap",
            justify_content="space-around"
        )

# Lista de productos para mostrar en la sección
products = [
    {
        "image_url": "https://via.placeholder.com/150",
        "name": "Producto 1",
        "description": "Descripción del producto 1",
        "price": "19.99"
    },
    {
        "image_url": "https://via.placeholder.com/150",
        "name": "Producto 2",
        "description": "Descripción del producto 2",
        "price": "29.99"
    },
    {
        "image_url": "https://via.placeholder.com/150",
        "name": "Producto 3",
        "description": "Descripción del producto 3",
        "price": "39.99"
    }
]

# Crear un componente principal que incluya la sección de productos
class MainComponent(rx.Component):
    def render(self):
        return rx.View(
            rx.Text("Sección de Productos", font_size=24, font_weight="bold", margin=20),
            ProductSection(products).render()
        )

# Crear la aplicación Reflex
app = rx.App(MainComponent())
app.run()