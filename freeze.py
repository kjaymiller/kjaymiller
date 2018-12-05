from markdown import Markdown
from flask_frozen import Freezer
from flask_app import app
from pathlib import Path
from glob import glob
from blog_engine.render_post import render_post
from urllib.parse import quote

freezer = Freezer(app)


@freezer.register_generator
def blog_posts():
    yield {'JSON_FEED': 'blog'}

@freezer.register_generator
def post():
    content_path = Path('content')
    pages = content_path.glob('*.md')
    for page in pages:
        metadata = render_post(page)
        yield {'JSON_FEED': 'blog',
               'slug': quote(metadata['slug'])}

if __name__ == '__main__':
    freezer.freeze()
