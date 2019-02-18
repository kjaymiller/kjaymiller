import config
import json
import shutil
from pathlib import Path
from collections import defaultdict
from pages.paginate import write_paginated_pages
from pages import (
        Page, 
        BlogPost,
        MicroBlogPost,
        Collection,
        )
from pages.generators import gen_static 
from pages.writer import write_page, writer


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
    what_im_block = ({
        'playing': [
            {
                'title': "Hearthstone", 
                'url':'https://playhearthstone.com/en-us/', 
                'image':'https://dsc.cloud/kjmScreenshots/iu.jpeg',
                },
            {
                'title': 'Tetris99',
                'url': 'https://www.nintendo.com/games/detail/tetris-99-switch',
                'image':'https://kjaymiller.s3-us-west-2.amazonaws.com/images/sega_home_page-banner_4.jpg',
                },
            {
                'title': 'Puyo Puyo Tertris',
                'url': 'https://amzn.to/2RTv4oP',
                'image':'https://kjaymiller.s3-us-west-2.amazonaws.com/images/sega_home_page-banner_4.jpg',
                },
            {
                'title': 'Tetris Effect',
                'url': 'https://amzn.to/2Wo4BOX',
                'image':'https://kjaymiller.s3-us-west-2.amazonaws.com/images/nonvolcanic-unstatically-sloughy-fribbling.jpg',
                }
            ], 
        'reading': [
            {
                'title': 'The Bullet Journal Method',
                'url': 'https://bulletjournal.com/pages/book',
                'image': 'https://cdn.shopify.com/s/files/1/0882/3478/files/Book_1320dabd-bc26-436d-9bc3-0f1741e91716_1200x.png?v=1531840787',
                },
            ],
            })


    latest_posts = blog.pages[:4]
    latest_microposts = sorted(microblog.pages, 
            key=lambda page: page.date_published)[:3]
    return Page(template='index.html', 
            what_im_block=what_im_block, 
            featured_post=latest_posts[0],
            latest_microposts=latest_microposts, latest_posts=latest_posts[1:]).html

def pagination():
    page_groups = blog, microblog
    for page in page_groups:
        write_paginated_pages(page.name, page.paginate, path=page.output_path, template='blog_list.html')

def categorization():
    page_groups = blog, microblog
    for page in page_groups:
        category_filename = f'{page.output_path}/categories'
        category_path = Path(category_filename)
        category_path.mkdir(parents=True, exist_ok=True)
        write_page(f'{category_path}/all.html', Page(template='categories.html', topic_list=[c for c in page.categories]).html)

        for category in page.categories:
            write_page(f'{category_path}/{category}.html', Page(template='blog_list.html', post_list=page.categories[category], output_path=page.output_path).html)
        
        tag_path = Path(f'{page.output_path}/tag')
        tag_path.mkdir(parents=True, exist_ok=True)
        write_page(f'{tag_path}/all.html', Page(template='categories.html', topic_list=[t for t in page.tags]).html)
        for tag in page.tags:
            write_page(f'{tag_path}/{tag}.html', Page(template='blog_list.html', post_list=page.categories[category], output_path=page.output_path).html)


def feed_gen():
    page_groups = blog, microblog 
    for page in page_groups:
        with open(f'{page.output_path}/{page.name}.json', 'w') as fp:
            json.dump(page.json_feed, fp)

        with open(f'{page.output_path}/{page.name}.rss', 'w') as rss:
            rss.write(page.rss_feed)
index()
categorization()
pagination()
feed_gen()
