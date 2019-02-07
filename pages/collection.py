import config
import json
from collections import defaultdict
from itertools import zip_longest
from pages import Page 
from pathlib import Path
import arrow

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
        self.json_feed = self.generate_from_metadata()

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


    def generate_from_metadata(self, config=config, **kwargs):
        feed_data = {
                'title': kwargs.get('title', config.SITE_TITLE),
                'home_page_url': kwargs.get('home_page_url', config.SITE_URL),
                'feed_url': kwargs.get('feed_url'),
                'version': kwargs.get('version', 'https://jsonfeed.org.version/1'),
                'icon': kwargs.get('icon', config.ICON),
                'description': kwargs.get('description', config.SITE_SUBTITLE),
                'user_comment': kwargs.get('user_comment'),
                'next_url': kwargs.get('next_url', ), # needs pagination
                'favicon': kwargs.get('favicon', config.FAVICON),
                'author': kwargs.get('author',{
                        'name': config.AUTHOR,
                        'avatar': config.AUTHOR_IMAGE,
                        'url': config.AUTHOR_URL,
                        }),
                'expired': kwargs.get('expired'),
                'hubs': kwargs.get('hubs'),
                }

        filled_feed_data = {x:y for x,y in feed_data.items() if y}

        feed_items = []

        filled_feed_data['items'] = [self.item_values(feed_item) for feed_item in self.pages]
        return filled_feed_data

    def item_values(self, item):

        items_values = {
           'id':item.id,
           'url': f'{self.output_path}/{item.id}',
           'title': item.title,
           'content_html': item.markup, 
           'summary': item.summary,
           'date_published': arrow.get(item.date_published, config.TIME_FORMAT).isoformat(),
           'date_modified': arrow.get(item.date_modified, config.TIME_FORMAT).isoformat(),
           } 

        other_item_values = (
                ('image', config.DEFAULT_POST_IMAGE), 
                ('banner_image', config.DEFAULT_POST_BANNER),
                ('author', None), 
                ('external_url', None),
            )
        
        for other_value in other_item_values:
            if other_value[0] in item.__dict__.keys():
                item_values[other_value[0]] = item.__dict__[other_value[0]]
            elif other_value[1]:
                item_values[other_value[0]] = other_value[1]
            else:
                continue
        return items_values
