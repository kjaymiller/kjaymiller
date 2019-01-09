import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
import generators


pages = ContentPath(
        name = 'pages',
        content_type = Page,
        )

blog = ContentPath(
        name = 'blog',
        content_type = BlogPost,
        content_path = 'content',
        )

microblog = ContentPath(
        name = 'microblog',
        content_type = MicroBlogPost,
        )

podcast = ContentPath(
        name = 'podcast',
        content_type = PodcastEpisode,
        )

PATHS = (pages, blog, podcast, microblog)

generators.generate(PATHS)
page =  Page(template='index.html').html
generators.write_page('index', page)
