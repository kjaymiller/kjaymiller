"""
Step 1 - Scans the content folder for '.md' and '.markdown' files

Step 2 - Check 'blog/'filename'.html' for already processed files.

Step 3a - If 2 == False, Parse Markdown and Save as blog/filename.html
Step 3b - If 2 == True, Skip and go to the next file
"""

from blog_engine.render_post import render_post
from pathlib import Path
import json
import string


class JSON_Feed():
    def __init__(self, json_file, content_path):
        self.json_file = json_file
        self.json_object = self.add_json_content(content_path.glob('*.md'))
        latest = sorted(self.json_object,
                        key=lambda x: self.json_object[x]['date'],
                        reverse=True)[:3]
        self.latest = [self.json_object[x] for x in latest]


    def add_json_content(self, content_path):
        json_object = {}
        for md_file in content_path:
            metadata = render_post(md_file)
            json_object[metadata['slug']] = metadata
        return json_object

class Blog(JSON_Feed):
     def check_for_json_file(json_file):
         if not Path(json_file).exists():
            with open(json_file) as f:
                return f.write('')


