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
from render_engine.feeds import path_crawler
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
        Path(f'{config.OUTPUT_PATH}/{p.output_path}').mkdir(parents=True)
        file_path = p.content_path
        files = path_crawler(item_type=p.content_type, file_path=file_path) 
        for i in files:
            write_page(f'{p.output_path}/{i.id}', i.html)
        
        pages = paginate.paginate(files, 10)
        paginate.write_paginated_pages(p.name, pages, 'blog_list.html', post_list=files)

if __name__=="__main__":
    generate()
