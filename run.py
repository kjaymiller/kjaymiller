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


pages = Collection(
        name = 'pages',
        content_type = Page,
        content_path = 'pages',
        )

blog = Collection(
        name = 'blog',
        content_type = BlogPost,
        output_path = 'blog',
        )

microblog = Collection(
        name = 'microblog',
        content_type = MicroBlogPost,
        content_path = 'microblog',
        )

shutil.rmtree(Path(config.OUTPUT_PATH))

@writer(route='index')
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

    latest_posts = sorted(blog_posts['pages'], key=lambda page: page.date_published, reverse=True)
    latest_microposts = sorted(microblog_posts['pages'], key=lambda page: page.date_published, reverse=True)
    return Page(template='index.html', podcast_block=podcast_block, latest_microposts=latest_microposts, latest_posts=latest_posts).html
index()

# Create Category and Tags
topics = ((blog_posts, 'categories'),
        (blog_posts, 'tags'),
        (microblog_posts, 'categories'),
        (microblog_posts, 'tags'))


def topic(topic, topic_list):
    return Page(template='categories.html', topic_list=topic[topic_list]).html

for _ in topics:
    output_path = _[0]['output_path']
    write_page(f'{output_path}/{_[1]}', topic(_[0], _[1]))
