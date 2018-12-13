"""
Step 1 - Scans the content folder for '.md' and '.markdown' files

Step 2 - Check 'blog/'filename'.html' for already processed files.

Step 3a - If 2 == False, Parse Markdown and Save as blog/filename.html
Step 3b - If 2 == True, Skip and go to the next file
"""

from blog_engine.render_post import render_post
from pathlib import Path
import json
import arrow
import string


class JSON_Feed():
    def __init__(self, content_path, title=True):
        self.content_path = Path(content_path).glob('*.md')
        self.json_object = self.__add_json_content__(self.content_path, title)

    def __add_json_content__(self, content_path, title=True):
        json_object = {}
        for md_file in content_path:
            metadata = render_post(md_file, title=title)
            json_object[metadata['slug']] = metadata
        return json_object

    def sorted_items(self, item_count=None):
        latest = sorted(self.json_object,
                        key=lambda x:
                        arrow.get(self.json_object[x]['date_published']),
                        reverse=True)[:item_count] # the default 'None' will cause all items to return
        return [self.json_object[x] for x in latest]


class Blog(JSON_Feed):
    def __init__(self, content_path, title=True, **kwargs):
        super().__init__(content_path, title=title)
        self.json_base = kwargs.get('json_base', '')
        self.json_filename = kwargs.get('json_filename', '')
        self.json_title = kwargs.get('json_title', '')

    def create_feed(self):
        with open(self.json_base) as f:
            feed = json.load(f)
        feed['title'] = self.json_title
        feed['items'] = self.sorted_items()
        for item in feed['items']:
            item.pop('slug')
        return feed


    def write_feed(self):
        with open(f'static/{self.json_filename}', 'w') as outfile:
            json.dump(self.create_feed(), outfile)
            outfile.truncate()


class MicroBlog(Blog):
    def __init__(self, content_path, title=False, **kwargs):
        super().__init__(content_path, title=title, **kwargs)
