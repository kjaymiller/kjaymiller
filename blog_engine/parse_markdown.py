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

    def sorted_items(self, item_count=-1):
        latest = sorted(self.json_object,
                        key=lambda x:
                        arrow.get(self.json_object[x]['date_published']),
                        reverse=True)[:item_count]
        return [self.json_object[x] for x in latest]


class Blog(JSON_Feed):
    def __init__(self, content_path, title=True, **kwargs):
        super().__init__(content_path, title=True)
        json_base = kwargs.get('json_base', '')
        json_filename = kwargs.get('json_filename', '')
        json_title = kwargs.get('json_title', '')

        if all((json_base, json_filename, json_title)):
            self.json_file = self.create_feed(json_base, json_title)
            self.write_feed(self.json_file, json_filename)

    def create_feed(self, json_base, title):
        with open(json_base) as f:
            feed = json.load(f)
        feed['items'] = self.sorted_items()
        return feed


    def write_feed(self, feed, filename):
        with open(f'static/{filename}', 'w') as outfile:
            json.dump(feed, outfile)
            outfile.truncate()


class MicroBlog(Blog):
    def __init__(self, content_path, **kwargs):
        super().__init__(content_path, title=False, **kwargs)
