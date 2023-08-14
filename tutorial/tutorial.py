"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from . import common as cm
from .front import front
from .demo import demo
from .gallery import gallery

# Add state and page to the app.
app = rx.App(state=cm.RootState)
app.add_page(front, route='/')
app.add_page(demo, route='/demo')
app.add_page(gallery, route='/gallery')
app.compile()
