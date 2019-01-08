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
from dataclasses import dataclass

@dataclass
class path:
    name: str
    content_type: Page
    content_path: Path
    output_path: Path


def generate(paths):
    # Remove output directory if it exists
    if Path(config.OUTPUT_PATH).exists():
        shutil.rmtree('output')

    # Create Static Files
    shutil.copytree(Path('./static/'), Path('./output/static/'))


    for p in paths:
        Path(p).mkdir(parents=True)

    for p in PATHS:
        file_path = p.content_path
        files = path_crawler(item_type=p.content_type, file_path=file_path) 
        for i in files:
            try: 
                write_page(f'{p.output_path}/{i.id}', i.html)
            except:
                continue
        
        pages = paginate.paginate(files, 10)
        paginate.write_paginated_pages(pages, 'blog_list.html')

if __name__=="__main__":
    generate()
