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
        content_path = 'microblog',
        )

PATHS = (pages, blog, microblog)

generators.generate(PATHS) #TODO: Doesn't Render Pages priority:High

index =  Page(template='index.html').html
generators.write_page('index', index)

print('Ran Successfully')
