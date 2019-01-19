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


def generate(paths):
    # Remove output directory if it exists
    try:
        shutil.rmtree(config.OUTPUT_PATH)
    except:
        pass
    
    # Create Static Files
    shutil.copytree(Path(config.STATIC_PATH),
            Path(f'{config.OUTPUT_PATH}/{config.STATIC_PATH}')
            )

    for p in paths:
        file_path = Path(f'{config.OUTPUT_PATH}/{p.output_path}')
        file_path.mkdir(parents=True)
        files = [item for item in p.content_path.glob(f'*{p.extension}')]
        print(files)
        for i in files:
            page = p.content_type(base_file=i)
            write_page(f'{p.output_path}/{page.id}', page.html)
        
        pages = paginate.paginate(files, 10)
        paginate.write_paginated_pages(p.name, pages, 'blog_list.html', post_list=files)

if __name__=="__main__":
    generate()
