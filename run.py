import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
import generators


pages = ContentPath(
        name = 'pages',
        content_type = Page,
        content_path = 'pages',
        paginate = False,
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

generators.generate(PATHS) #TODO: Doesn't Render Pagination Items

podcast_block = (
            {
            'title': 'Productivity in Tech Podcast',
            'url': 'https://productivityintech.transistor.fm',
            }, 
            {
            'title': 'Dev Otaku',
            'url':'https://devotaku.transistor.fm',
                }, 
            {
            'title': 'Ask a Brit',
            'url': 'https://askabrit.us',
            }
            )
index =  Page(template='index.html', podcast_block=podcast_block).html
generators.write_page('index', index)

print('Ran Successfully')
