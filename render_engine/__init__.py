import arrow
from config import REGION
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml'])
            )

def get_ct_time(md_file):
    return arrow.get(md_file.stat().st_ctime, tzinfo=REGION).isoformat()

def get_md_time(md_file):
    return arrow.get(md_file.stat().st_mtime, tzinfo=REGION).isoformat()
