from string import punctuation
from flask import Markup
from markdown import markdown
from dateutil.parser import parse
from datetime import datetime
from config import REGION

import arrow

def get_md_time(md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=REGION).isoformat()

def render_post(md_file, title=True):
    with md_file.open() as f:
        md_content = f.read()
    line_splitter = 0
    metadata = {}
    while ':' in md_content.split('\n')[line_splitter]:
        line = md_content.split('\n')[line_splitter]
        line_splitter += 1
        line_data = line.split(':', 1)
        metadata[line_data[0].lower()] = line_data[-1].strip()
    post = '\n'.join(md_content.split('\n')[line_splitter:])

    # If Date is not defined, you must pull it from the file.
    # If it is defined you need to convert it to a datetime object.
    if 'date' in metadata:
        metadata['date_published'] = arrow.get(parse(metadata['date'])).isoformat()
    else:
        metadata['date_published'] = get_md_time(md_file)

    metadata['content_html'] = Markup(markdown(post))
    if title:
        metadata['title'] = metadata.get('title', md_file.stem)
        metadata['slug'] = metadata.get('slug', metadata['title']).replace(' ','-')
    else:
        metadata['title'] = ''
        metadata['slug'] = metadata['date_published']

    if 'summary' not in metadata:
        start_index = min(280, len(metadata['content_html'])-1)
        while metadata['content_html'][start_index] not in punctuation:
            start_index -= 1
        metadata['summary'] = metadata['content_html'][:start_index + 1] + '...'

    metadata['summary'] = Markup(metadata['summary'])

    return metadata
