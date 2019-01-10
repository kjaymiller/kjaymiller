import config
from render_engine.content import Page
from pathlib import Path

class ContentPath:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.content_type = kwargs.get('content_type')
        content_path = kwargs.get('content_path', '')
        self.content_path = Path(f'{config.CONTENT_PATH}/{content_path}')
        output_path = kwargs.get('output_path', self.name)
        self.output_path = Path(f'{output_path}')
