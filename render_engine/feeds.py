"""
Feeds takes objects and creates an arrangement of items and returns a feed.
"""
import json
from pathlib import Path
from render_engine import env
import config

self.items = [item_type(base_file=item) for item in Path(file_path).glob(f'*{extension}')]

class PathCrawler:
    def __init__(self, item_type, file_path, extension='.md', **kwargs):
        """Takes a path and parses the files to create the item index"""
        self.json_feed = self.JSONFeed_metadata(**kwargs)
        self.json_feed['items'] = self.JSON_feed_items()

    def JSONFeed_metadata(self, **kwargs):
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
       
        return json.dumps(filled_feed_data)


    def JSON_feed_items(self, items, path):
        feed_items = []
        for item in items:
            items_values = {
               'id':item.id,
               'url': f'{path}/{item.id}',
               'external_url': item.external_url,
               'title': item.title,
               'content_html': item.markup, 
               'summary': item.summary,
               'date_published': item.date_published,
               'date_modified': item.date_modified,
               } 

            other_item_values = (
                    ('image', config.DEFAULT_POST_IMAGE), 
                    ('banner_image', config.DEFAULT_POST_BANNER),
                    ('author', None) 
                )
            
            for other_value in other_item_values:
                if other_value[0] in other.__dict__.keys():
                    item_values[other_value[0]] = item.__dict__[other_value[0]]
                elif other_value[1]:
                    item_values[other_value[0]] = other_value[1]
                else:
                    continue

            feed_items.append(item_values)
        return feed_items 
