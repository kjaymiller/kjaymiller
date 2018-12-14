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


class Page():
    def __init__(self, base_file, **kwargs):
        metadata = {}
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
        metadata['id'] = metadata.get('id', base_file.stem)
        metadata['title'] = metadata.get('title', '')
        self.metadata = metadata

"""
        metadata['date_published'] = get_ct_time(md_file)
        metadata['date_modified'] = get_md_time(md_file)

        if title:
            metadata['title'] = metadata.get('title', '')
        else:
            metadata['title'] = ''

        if 'summary' not in metadata:
            start_index = min(280, len(metadata['content_html'])-1)
            while metadata['content_html'][start_index] not in punctuation:
                start_index -= 1
            metadata['summary'] = metadata['content_html'][:start_index + 1] + '...'
        metadata['summary'] = Markup(metadata['summary'])
"""
