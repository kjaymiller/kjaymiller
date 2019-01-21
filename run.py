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

pages = generate(pages)
blog_posts = generate(blog)
microblogs = generate(microblog)

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
latest_posts = sorted(blog_posts, page.date_published, reverse=True)
index =  Page(template='index.html', podcast_block=podcast_block, latest_posts=latest_posts).html
write_page('index', index)

print('Ran Successfully')
