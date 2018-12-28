from markdown import Markdown
from flask_frozen import Freezer
from flask_app import app
from pathlib import Path
from glob import glob
from render_engine.content import (
        BlogPost, 
        MicroBlogPost,
        Page,
        PodcastEpisode,
        )
from render_engine.feeds import path_crawler
from collections import namedtuple
from urllib.parse import quote
import config

freezer = Freezer(app)


PATHS = {
        'pages': Page,
        'blog' : BlogPost, 
        'podcast':  PodcastEpisode, 
        'microblog': MicroBlogPost
        }

"""
@freezer.register_generator
def blog_posts():
    yield {'JSON_FEED': 'blog'}
"""

@freezer.register_generator
def post():
    for path in PATHS:
        PATH = PATHS[path]
        file_path = Path(config.BASE_PATH) / path
        files = path_crawler(item_type=PATH, file_path=file_path) 
        
        for i in files:
            yield {
                   'path': path,
                   'id': i.id,
                   'content': i.content,
                   'file_item': i,
                    }

if __name__ == '__main__':
    freezer.freeze()
