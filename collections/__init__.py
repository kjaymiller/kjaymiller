import config
from render_engine.content import Page
from pathlib import Path

class ContentPath:
    def __init__(self, paginate=True, categories=False, tags=False, **kwargs):
        self.name = kwargs.get('name')
        self.content_type = kwargs.get('content_type')
        self.extension = kwargs.get('extension', '.md')
        content_path = kwargs.get('content_path', '')
        self.content_path = Path(f'{config.CONTENT_PATH}/{content_path}')
        output_path = kwargs.get('output_path', self.name)
        self.output_path = Path(f'{output_path}')
        self.paginate = paginate
        self.categories = categories
        self.tags = tags 
