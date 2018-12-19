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


class Page():
    def __init__(self, base_file: Path):
        self.base_file = base_file
        with base_file.open() as f:
            md_content = [line.strip('\n') for line in f.readlines()]

        match = r'^\w+:'
        while re.match(match, md_content[0], flags=re.MULTILINE):
            line = md_content.pop(0)
            line_data = line.split(': ', 1)
            key = line_data[0].lower()
            value = line_data[-1]
            setattr(self, f'_{key}', value)

        self.title = self.get_title()
        self.id = self.get_id()
        self.tags = self.get_tags()
        self.content = '\n'.join(md_content)
        self.summary = self.get_summary()
        self.__str__ = self.content

    def _get_ct_time(self, md_file):
        return arrow.get(md_file.stat().st_ctime, tzinfo=REGION).isoformat()

    def _get_md_time(self, md_file):
        return arrow.get(md_file.stat().st_mtime, tzinfo=REGION).isoformat()


    def get_title(self):
        """Returns the value of _title, or an empty title if not defined"""
        return getattr(self, '_title', '')

    def get_id(self): 
        """Returns the value of _id.
        If there is no _id, it returns the value for _slug.
        If neither, it return the stem of the filepath."""

        if hasattr(self, '_id'):
            return self._id
        elif hasattr(self, '_slug'):
            return self._slug
        else:
             return self.base_file.stem

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
             return self._get_ct_time(base_file)

    def get_date_modified(self, base_file):
        """Returns the value of _date_modified or _update, or the
        modified_datetime from
        the system if not defined. NOTE THE SYSTEM DATE IS KNOWN TO CAUSE
        ISSUES WITH FILES THAT WERE COPIED OR TRANSFERRED WITHOUT THEIR
        METADADTA BEING TRANSFERRED AS WELL"""

        if hasattr(self, '_date_modified'):
            return self._date_modified
        
        elif hasattr(self, '_updated'):
            return self._date
        
        else:
            return self._get_mt_time(base_file)

    def get_tags(self):
        tags = getattr(self, '_tags', '')
        return tags.split(',')

    def _summary_from_content(self):
        start_index = min(280, len(self.content)-1)
        while self.content[start_index] not in punctuation:
                start_index -= 1
        return self.content[:start_index]

    def get_summary(self):
        return getattr(self, '_summary', self._summary_from_content()) + '...' 

