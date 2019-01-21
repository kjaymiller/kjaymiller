import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
from generators import generate, write_page


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

generate(pages)
generate(blog)
generate(microblog)

podcast_block = (
            {
            'title': 'Productivity in Tech Podcast',
            'url': 'https://productivityintech.transistor.fm',
            'img': '',
            }, 
            {
            'title': 'Dev Otaku',
            'url':'https://devotaku.transistor.fm',
            'img':'',
            }, 
            {
            'title': 'Ask a Brit',
            'url': 'https://askabrit.us',
            'img': '',
            }
            )
index =  Page(template='index.html', podcast_block=podcast_block).html
write_page('index', index)

print('Ran Successfully')
