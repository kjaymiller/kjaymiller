import config
from collections import defaultdict
from itertools import zip_longest
from pages import Page
from pathlib import Path

class Collection:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.content_type = kwargs.get('content_type')
        self.extension = kwargs.get('extension', '.md')
        content_path = kwargs.get('content_path', '')
        self.content_path = Path(f'{config.CONTENT_PATH}/{content_path}')
        self.output_path = Path(f'{config.OUTPUT_PATH}/'+ kwargs.get('output_path', ''))
        page_glob = self.content_path.glob('*.md')
        pages = [self.content_type(base_file=p) for p in page_glob]
        self.pages = sorted(pages, key=lambda page: page.date_published, reverse=True)

    @property
    def paginate(self):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(self.pages)] * 10
        iterable = zip_longest(*args, fillvalue=None) 
        return iterable
        
    @property
    def categories(self):
        d = defaultdict(list)
        for p in self.pages:
            d[p._category].append(p) 
        return d

    @property
    def tags(self):
        d = defaultdict(list)
        for p in self.pages:
            for tag in p.tags:
                d[tag].append(p)
        return d
