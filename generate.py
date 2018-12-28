from render_engine.content import Page
import generators

generators.generate()

def index():
    return Page(template='index.html')

index()


