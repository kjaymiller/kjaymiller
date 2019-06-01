import config
import json
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from pages.generators import gen_static
from pages.writer import write_page, writer
from blocks import what_im_block




shutil.rmtree(Path(config.OUTPUT_PATH), ignore_errors=True)

# build static pages
gen_static()
for collection in config.CONTENT_TYPES:
    collection.output_path.mkdir(parents=True, exist_ok=True)
    for page in collection.pages:
        write_page(f'{collection.output_path}/{page.id}.html', page.html)

@writer(route='index.html')
def index():
    latest_posts = blog.pages[:4]

    return Page(template='index.html',
            what_im_block=what_im_block,
            featured_post=latest_posts[0],
            latest_posts=latest_posts[1:]).html

def pagination():
    page_groups = config.PAGINATION

    for page in page_groups:
        write_paginated_pages(page.name, page.paginate, path=page.output_path, template='blog_list.html')

def categorization():
    page_groups = config.CATEGORIZED
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
    page_groups = config.PAGINATION
    for page in page_groups:
        with open(f'{page.output_path}/{page.name}.json', 'w') as fp:
            json.dump(page.json_feed, fp)

        with open(f'{page.output_path}/{page.name}.rss', 'w') as rss:
            rss.write(page.rss_feed)
index()
categorization()
pagination()
feed_gen()
