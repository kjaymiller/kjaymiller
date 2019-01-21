"""
Generates the files to build out your HTML Path
"""
import os
import shutil
from writer import write_page
import paginate
from pathlib import Path
from render_engine.content import (
        BlogPost, 
        MicroBlogPost,
        Page,
        PodcastEpisode,
        )
# from render_engine.feeds import PathCrawler
import config


def generate(path):
    # Remove output directory if it exists
    try:
        shutil.rmtree(config.OUTPUT_PATH)
    except:
        pass
    
    # Create Static Files
    shutil.copytree(Path(config.STATIC_PATH),
            Path(f'{config.OUTPUT_PATH}/{config.STATIC_PATH}')
            )

    file_path = Path(f'{config.OUTPUT_PATH}/{path.output_path}')
    file_path.mkdir(parents=True)
    files = [item for item in path.content_path.glob(f'*{path.extension}')]
    pages = []

    # write page
    for i in files:
        page = path.content_type(base_file=i)
        write_page(f'{path.output_path}/{page.id}', page.html)
        pages.append(page) 
    
    if path.paginate:
        paginate.write_paginated_pages(
                name = path.name, 
                pagination = paginate.paginate(pages, 10), 
                template = 'blog_list.html', 
                post_list=pages) #THIS SHOULD BE THE LIST OF FILES (f.name, f.id)
    return pages
if __name__=="__main__":
    generate()
