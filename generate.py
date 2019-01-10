import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
import generators


pages = ContentPath(
        name = 'pages',
        content_type = Page,
        content_path = 'pages'
        )

blog = ContentPath(
        name = 'blog',
        content_type = BlogPost,
        )

microblog = ContentPath(
        name = 'microblog',
        content_type = MicroBlogPost,
        )

PATHS = (pages, blog, microblog)

generators.generate(PATHS)
page =  Page(template='index.html').html
generators.write_page('index', page)
