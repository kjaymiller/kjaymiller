from render_engine.valid_keys import JSON_keys
from string import punctuation
from flask import Markup
from markdown import markdown
from dateutil.parser import parse
from datetime import datetime
from config import REGION

import arrow
import re

def get_ct_time(md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=REGION).isoformat()

def get_md_time(md_file):
    return arrow.get(md_file.stat().st_mtime, tzinfo=REGION).isoformat()


def alt_keys(holder, optional_keys, system_default):
    """
    Because this will hopefully replace many different types of content. There is a need for translations.

    'holder' is the what holds the keys.
    'optional_keys' = (iterable) an array of other keys that would be accepted.
    """
    for optional_key in optional_keys:
        if optional_key in holder:
            return holder[optional_key]
    
    return system_default        

class Page():
    def __init__(self, base_file, **kwargs):
        metadata = {}
        self.base_file = base_file
        with base_file.open() as f:
            md_content = f.read()
        line_splitter = 0
        metadata = {}
        md_lines = md_content.split('\n')

        match = r'^\w+:'
        while re.match(match, md_lines[line_splitter], flags=re.MULTILINE): 
            line = md_lines[line_splitter]
            line_splitter += 1

            line_data = line.split(':', 1)
            key = line_data[0].lower()
            metadata[key] = line_data[-1].strip()

            # if key in json_feed_keys:
            #    metadata[key] = line_data[-1].strip()

        # post = '\n'.join(md_lines[line_splitter:])
        # self.'content_html' = Markup(markdown(post))

        metadata['title'] = metadata.get('title', '')
        metadata['id'] = metadata.get('id', 
                alt_keys(metadata, ['slug'], base_file.stem))
        metadata['date_published'] = get_ct_time(md_file)
        metadata['date_modified'] = get_md_time(md_file)
"""
        if 'summary' not in metadata:
            start_index = min(280, len(metadata['content_html'])-1)
            while metadata['content_html'][start_index] not in punctuation:
                start_index -= 1
            metadata['summary'] = metadata['content_html'][:start_index + 1] + '...'
        metadata['summary'] = Markup(metadata['summary'])
        """
        self.metadata = metadata
