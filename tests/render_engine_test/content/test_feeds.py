import json
from pathlib import Path
import pytest
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from render_engine.feeds import JSONFeed

class TestJSONFeed():
    """This is the root feed that takes a collection of similar content objects"""
    
    standard_json_feed = JSONFeed(
            avatar = '',
            version = '',
            items  =  ['foo', 'bar'],
            author =  '',
            title = '',
            feed_url = '',
            home_page_url = '',
            icon = '',
            favicon = '',
            description = '',
            hubs = ''
            )

    def test_title_in_json_feed(self):
        assert self.standard_json_feed.title == ''

    def test_items_in_json_feed(self):
        assert self.standard_json_feed.items == ['foo', 'bar']

    def test_home_page_url(self):
        assert self.standard_json_feed.home_page_url == ''
    
    def test_url_in_json_feed(self):
        assert self.standard_json_feed.feed_url == ''

    def test_version_in_json_feed(self):
        assert self.standard_json_feed.version == ''

    def test_description_in_json_feed(self):
        assert self.standard_json_feed.description == ''

    def test_favicon_in_json_feed(self):
        assert self.standard_json_feed.favicon == ''

    def test_icon_in_json_feed(self):
        assert self.standard_json_feed.icon == ''

    def test_expired_in_json_feed(self):
        assert self.standard_json_feed.expired == False

    def test_author_in_json_feed(self):
        assert self.standard_json_feed.author == ''

    def test_avatar_in_json_feed(self):
        assert self.standard_json_feed.avatar == ''

    def test_hubs_in_json_feed(self):
        assert self.standard_json_feed.hubs == ''

    def test_from_file_in_json_feed(self, tmpdir):
        from_file = tmpdir.join('from_file.md')
        json_data = {
                "title":"test title", 
                "feed_url":"another_test",
                "items":['foo', 'bar']
                }
        with open(from_file, 'w') as f:
            json.dump(json_data, f)
        feed = JSONFeed(from_file=from_file)
        assert feed.title == 'test title'
        assert feed.feed_url == 'another_test'

    def test_str_from_file_in_json_feed(self):
        assert self.standard_json_feed.__dict__
