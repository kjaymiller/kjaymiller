"""
This is how all of the information is compiled into lists to be added to Feeds
"""
from pathlib import Path
from render_engine.feeds import JSONFeed


def path_crawler(item_type, file_path, extension='.md'):
    """
    Takes a path and parses the files to create the item index
    """
    items = [item_type(base_file=item) for item in Path(file_path).glob(f'*.{extension}')]
    return items


def new_JSONFeed(path, template_file):
    return JSONFeed
