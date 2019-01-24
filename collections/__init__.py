import config
from pages.content import Page
from pathlib import Path

class Collection:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.content_type = kwargs.get('content_type')
        self.extension = kwargs.get('extension', '.md')
        content_path = kwargs.get('content_path', '')
        self.content_path = Path(f'{config.CONTENT_PATH}/{content_path}')
        output_path = kwargs.get('output_path', self.name)
        self.output_path = Path(f'{output_path}')
        pages = self.content_path.glob('*.md')
        self.pages = [self.content_type(base_file=p) for p in pages]
                
    @property
    def paginate(self):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(self.pages)] * 10
        iterable = zip_longest(*args, fillvalue=None) 
        return iterable
        
    @property
    def categories(self):
        return set((p._category for p in self.pages))

    @property
    def tags(self):
        tag_list = set()
        for p in self.pages:
            tag_list.update(set((tag for tag in p.tags)))
        return tag_list
