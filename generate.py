from render_engine.content import Page
import generators

generators.generate()

def index():
    page =  Page(template='index.html').html
    return generators.write_page('output', 'index', page)
index()


