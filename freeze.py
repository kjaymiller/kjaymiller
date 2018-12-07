from markdown import Markdown
from flask_frozen import Freezer
from flask_app import app
from pathlib import Path
from glob import glob
from blog_engine.render_post import render_post
from collections import namedtuple
from urllib.parse import quote

freezer = Freezer(app)


@freezer.register_generator
def blog_posts():
    yield {'JSON_FEED': 'blog'}

@freezer.register_generator
def post():
    path = namedtuple('path',['dirName', 'dirPath'])
    blog = path('blog', Path('content'))
    pages = path('pages', Path('content/pages'))
    microblog = path('microblog', Path('content/mircoblog'))
    paths = [blog, pages, microblog]

    for path in paths:
        pages = path.dirPath.glob('*.md')
        for page in pages:
            metadata = render_post(page)
            yield {
                   'JSON_FEED': path.dirName,
                   'slug': quote(metadata['slug'])
                    }

if __name__ == '__main__':
    freezer.freeze()
