import re
import config
from pathlib import Path
from render_engine.valid_keys import JSON_keys
from render_engine.__init__ import env, get_md_time, get_ct_time
from string import punctuation
from jinja2 import Markup
from markdown import markdown
from dateutil.parser import parse
from datetime import datetime

import arrow

class Page():
    def __init__(self, base_file=None, template='page.html'):
        # self.id looks for us
        self._id = None
        self._slug = None
        self.template = template
        # self.date_published looks for us
        self._date_published = None
        self._date = None
        self.base_file = base_file
        
        if base_file:
            self.from_file(base_file) # creates initial properties and self.content

        temp =  env.get_template(self.template)
        self.html = temp.render(metadata=self, config=config)
        
    def from_file(self, base_file):
        matcher = r'^\w+:'
        with open(base_file) as f:
            md_content = f.readlines()
            while re.match(matcher, md_content[0]):
                line = md_content.pop(0)
                line_data = line.split(': ', 1)
                key = line_data[0].lower()
                value = line_data[-1].rstrip()
                setattr(self, f'_{key}', value)
            content = '\n'.join(md_content).strip()
            self.content = content
            self.markup = Markup(markdown(content))

        self.title = getattr(self, '_title', '')
        self.__str__ = self.content
        temp =  env.get_template(self.template)
        self.html = temp.render(metadata=self, config=config)

    @property
    def id(self):
        return self._id or self._slug or self.base_file.stem

    @property
    def date_published(self):
        """Returns the value of _date_published or _date, or created_datetime from
the system if not defined. NOTE THE SYSTEM DATE IS KNOWN TO CAUSE
ISSUES WITH FILES THAT WERE COPIED OR TRANSFERRED WITHOUT THEIR
METADATA BEING TRANSFER READ AS WELL"""

        if self._date_published:
            return self._date_published

        elif '_date':
            return self._date

        else:
             return get_ct_time(self.base_file)

    @property
    def updated(self):
        """Returns the value of _date_modified or _update, or the
modified_datetime from the system if not defined. NOTE THE SYSTEM 
DATE IS KNOWN TO CAUSE ISSUES WITH FILES THAT WERE COPIED OR 
TRANSFERRED WITHOUT THEIR METADADTA BEING TRANSFERRED AS WELL"""

        if self._date_modified:
            return self._date_modified
        
        elif self.updated:
            return self._date

        else:
            return get_mt_time(self.base_file)


class BlogPost(Page):
    def __init__(self, base_file, template='blog.html'):
        super().__init__(base_file, template=template)
        self.tags = self.get_tags()
        self.summary = Markup(markdown(getattr(self, '_summary',
                self.summary_from_content(self.content)) + '...'))

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
    def __init__(self, base_file, podcast_name: str, episode_number: int):
        super().__init__(base_file)

    
