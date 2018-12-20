from pathlib import Path
from render_engine.valid_keys import JSON_keys
from string import punctuation
from flask import Markup
from markdown import markdown
from dateutil.parser import parse
from datetime import datetime
from config import REGION

import arrow
import re


def get_ct_time(self, md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=region).isoformat()

def get_md_time(self, md_file):
    return arrow.get(md_file.stat().st_mtime, tzinfo=region).isoformat()

class Page():
    def __init__(self, base_file):
        # self.id looks for us
        self._id = None
        self._slug = None

        # self.date_published looks for us
        self._date_published = None
        self._date = None

        self.base_file = base_file
        self.load_from_file(self.base_file) # creates initial properties and self.content

        
        self.title = getattr(self, '_title', '')
        self.__str__ = self.content

    def load_from_file(self, base_file):
        matcher = r'^\w+:'
        with base_file.open() as f:
            md_content = f.readlines()
            while re.match(matcher, md_content[0]):
                line = md_content.pop(0)
                line_data = line.split(': ', 1)
                key = line_data[0].lower()
                value = line_data[-1].rstrip('\n')
                setattr(self, f'_{key}', value)
            self.content = '\n'.join(md_content).strip()

    @property
    def id(self):
        return self._id or self._slug or self.base_file.stem

    def get_date_published(self, base_file):
        """Returns the value of _date_published or _date, or created_datetime from
        the system if not defined. NOTE THE SYSTEM DATE IS KNOWN TO CAUSE
        ISSUES WITH FILES THAT WERE COPIED OR TRANSFERRED WITHOUT THEIR
        METADATA BEING TRANSFER READ AS WELL"""

        if hasattr(self, '_date_published'):
            return self._date_published
        elif hasattr(self, '_date'):
            return self._date
        else:
             return self.get_ct_time(base_file)

    def get_date_modified(self, base_file):
        """Returns the value of _date_modified or _update, or the
modified_datetime from the system if not defined. NOTE THE SYSTEM 
DATE IS KNOWN TO CAUSE ISSUES WITH FILES THAT WERE COPIED OR 
TRANSFERRED WITHOUT THEIR METADADTA BEING TRANSFERRED AS WELL"""

        if hasattr(self, '_date_modified'):
            return self._date_modified
        
        elif hasattr(self, 'updated'):
            return self._date
        
        else:
            return self._get_mt_time(base_file)

class BlogPost(Page):
    def __init__(self, base_file):
        super().__init__(base_file)
        self.tags = self.get_tags()
        self.summary = getattr(self, '_summary',
                self.summary_from_content(self.content)) + '...'


    def get_tags(self):
        tags = getattr(self, '_tags', '')
        return tags.split(',')

    def summary_from_content(self, content):
        print(len(content))
        start_index = min(280, len(content) - 1)
        print(start_index) 
        while content[start_index] not in punctuation:
            start_index -= 1
        
            if not start_index:
                  return content
              
        return self.content[:start_index]

class MicroBlogPost(BlogPost):
    title = ''
    def __init__(self, base_file):
        super().__init__(base_file)

class PodcastEpisode(BlogPost):
    def __init__(self, base_file, podcast_name: string, episode_number: int):
        super().__init__(base_file)

    
