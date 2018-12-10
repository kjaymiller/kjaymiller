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
    def __init__(self,
                 content_path,
                 json_base='',
                 json_filename='',
                 json_title=''):

        self.json_object = self.add_json_content(content_path.glob('*.md'))
        latest = sorted(self.json_object,
                        key=lambda x:
                        arrow.get(self.json_object[x]['date_published']),
                        reverse=True)[:3]
        self.latest = [self.json_object[x] for x in latest]
        
        if json_base:
            self.json_file = self.create_feed(json_base, json_filename, json_title)

    def add_json_content(self, content_path):
        json_object = {}
        for md_file in content_path:
            metadata = render_post(md_file)
            json_object[metadata['slug']] = metadata
        return json_object

    def create_feed(self, json_base, filename, title):
        with open(json_base) as f:
            feed = json.load(f)
        feed['title'] = title
        sorted_items = sorted(self.json_object,
                    key=lambda x:
                    arrow.get(self.json_object[x]['date_published']),
                    reverse=True)

        feed['items'] = [self.json_object[item] for item in sorted_items]
        with open(f'static/{filename}', 'w') as outfile:
            json.dump(feed, outfile)
            outfile.truncate()
         return feed


class MicroBlog(JSON_Feed):
    def create_feed(self, json_base, filename, title):
        with open(json_base) as f:
            feed = json.load(f)
        feed['title'] = title
        sorted_items = sorted(self.json_object,
                    key=lambda x:
                    arrow.get(self.json_object[x]['date_published']),
                    reverse=True)

        feed['items'] = [self.strip_title(self.json_object[item]) for item in sorted_items]
        with open(f'static/{filename}', 'w') as outfile:
            json.dump(feed, outfile)
            outfile.truncate()
         return feed

    def strip_title(self, metadata):
        metadata['title'] = ''
        return metadata
