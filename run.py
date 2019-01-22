import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
from writer import writer
from generators import generate, gen_static
import shutil



pages = ContentPath(
        name = 'pages',
        content_type = Page,
        content_path = 'pages',
        paginate = False,
        )

blog = ContentPath(
        name = 'blog',
        content_type = BlogPost,
        output_path = 'blog',
        )

microblog = ContentPath(
        name = 'microblog',
        content_type = MicroBlogPost,
        content_path = 'microblog',
        )

shutil.rmtree(Path(config.OUTPUT_PATH))

blog_categories = {}
microblog_categories = {}

pages = generate(pages)
blog_posts = generate(blog, category=blog_categories)
microblog_posts = generate(microblog, microblog_categories)


gen_static()

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

@writer(route='index')
def index():
    latest_posts = sorted(blog_posts, key=lambda page: page.date_published, reverse=True)
    latest_microposts = sorted(microblog_posts, key=lambda page: page.date_published, reverse=True)
    return Page(template='index.html', podcast_block=podcast_block, latest_microposts=latest_microposts, latest_posts=latest_posts).html

print('Ran Successfully')



index()
