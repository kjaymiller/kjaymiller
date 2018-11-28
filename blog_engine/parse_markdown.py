"""
Step 1 - Scans the content folder for '.md' and '.markdown' files

Step 2 - Check 'blog/'filename'.html' for already processed files.

Step 3a - If 2 == False, Parse Markdown and Save as blog/filename.html
Step 3b - If 2 == True, Skip and go to the next file
"""

from markdown import markdown
from pathlib import Path
import json

def render_post(md_content):
    post = md_content.split('\n\n', 1)
    metadata_string = post[0]
    metadata = {}

    for line in metadata_string.split('\n'): 
        line_data = line.split(': ', 1)
        metadata[line_data[0].lower()] = line_data[-1]

    metadata['content'] = markdown(post[-1])
    return metadata     

class JSON_Feed():
    def __init__(self, json_file, content_path, new=False):    
        self.json_file = json_file
        self.content_path = content_path.glob('*.md')
            
        if new:  
            self.slug_table = {}
            self.json_object = self.load_new_json_file(json_file, self.content_path)
        else:
            self.json_object = self.load_json_file(json_file)

    def add_json_content(self, json_object, content_path):
        for md_file in content_path:
            with open(md_file) as f:
                metadata = render_post(f.read())
            if 'title' in metadata:
                slug = metadata.get('slug', metadata['title'])
                if all([metadata['title'], slug]):
                    metadata['slug'] = slug     
                    self.slug_table[slug] = md_file.name
                    json_object['items'].append(metadata)
            else:
                continue 
        return json_object

    def load_json_file(self, json_file):
        with open(json_file) as f:
             return json.loads(f.read())

    def purge_json_items(self, json_object):
        new_object = json_object
        new_object['items'] = []
        return new_object
             
    def load_new_json_file(self, json_file, content_path):
        json_object = self.load_json_file(json_file)
        json_object_no_items = self.purge_json_items(json_object)
        return self.add_json_content(json_object_no_items, content_path)
            
        
class Blog(JSON_Feed):
     def check_for_json_file(json_file):
         if not Path(json_file).exists():
            with open(json_file) as f:
                return f.write('')
    
