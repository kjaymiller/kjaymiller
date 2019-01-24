import config
import shutil
from pathlib import Path
from Collections import Collection
from pages.content import (
        Page, 
        BlogPost,
        MicroBlogPost,
        PodcastEpisode,
        )
from generators import gen_static 
from writer import write_page, writer


pages = Collection(name='pages', content_type=Page, content_path='pages')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')
microblog = Collection(name='microblog', content_type=MicroBlogPost, content_path='microblog', output_path='microblog')

shutil.rmtree(Path(config.OUTPUT_PATH))

# build static pages
gen_static()
 
page_collections = pages, blog, microblog
for collection in page_collections:
    collection.output_path.mkdir(parents=True, exist_ok=True)
    for page in collection.pages:
        write_page(f'{collection.output_path}/{page.id}.html', page.html)

@writer(route='index.html')
def index():
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

    latest_posts = sorted(blog.pages, key=lambda page: page.date_published, reverse=True)
    latest_microposts = sorted(microblog.pages, key=lambda page: page.date_published, reverse=True)
    return Page(template='index.html', podcast_block=podcast_block, latest_microposts=latest_microposts, latest_posts=latest_posts).html
index()
