from markdown import Markdown
from flask_frozen import Freezer
from flask_app import app
from pathlib import Path
from glob import glob
from blog_engine.parse_markdown import JSON_Feed, Blog, MicroBlog
from collections import namedtuple
from urllib.parse import quote
import config

freezer = Freezer(app)


pages = JSON_Feed('content/pages')
blog = Blog('content',
            json_base='blog_feed.json',
            json_filename='blog.json',
            json_title=config.SITE_TITLE)
blog.write_feed()

micro = MicroBlog('content/microblog',
             json_base='micro_feed.json',
             json_filename='micro.json',
             json_title=f'{config.SITE_TITLE} - Microblog')
micro.write_feed()

feeds = {
        'pages': pages,
        'blog': blog,
        'microblog': micro,
        }

@freezer.register_generator
def blog_posts():
    yield {'JSON_FEED': 'blog'}

@freezer.register_generator
def post():
    for feed in feeds:
        json_object = feeds[feed].json_object
        for article in json_object:
            yield {
                   'JSON_FEED': feed,
                   'slug': article
                    }




if __name__ == '__main__':
    freezer.freeze()
