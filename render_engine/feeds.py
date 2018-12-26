"""
Feeds takes objects and creates an arrangement of items and returns a feed.
"""
import json

class JSONFeed():
    def __init__(self, items=[], expired=False, from_file=None, **kwargs):
        
        self.items = [item for item in items if items]
        self.title = kwargs.get('title')
        self.home_page_url = kwargs.get('home_page_url')
        self.feed_url = kwargs.get('feed_url')
        self.version = kwargs.get('version')
        self.icon = kwargs.get('icon')
        self.description = kwargs.get('description')
        self.user_comment = kwargs.get('user_comment')
        self.next_url = kwargs.get('next_url')
        self.favicon = kwargs.get('favicon')
        self.author = kwargs.get('author')
        self.avatar = kwargs.get('avatar')
        self.expired = expired
        self.hubs = kwargs.get('hubs')
        
        if from_file:
            with open(from_file) as f:
                json_content = f.read()
                base_file = json.loads(json_content)
            for key in base_file.keys():
                setattr(self, key, base_file[key])

        self.json = json.dumps(self.__dict__)
