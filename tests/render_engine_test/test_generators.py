from render_engine.content import Page, BlogPost, MicroBlogPost
import pytest
from render_engine.generators import path_crawler
from pathlib import Path


def test_paths(standard_file, standard_path):
    assert len([a for a in standard_path.iterdir()]) == 1


path_types = (
        Page, 
        BlogPost, 
        MicroBlogPost,
        )

class TestPathCrawler():
    @pytest.mark.parametrize('item_types', path_types)
    def test_path_crawler(
            self,
            standard_path, 
            item_types):
        assert path_crawler(item_type=item_types, file_path=standard_path)

    def test_path_crawler_accepts_path_items(self,standard_file,  standard_path):
        assert path_crawler(item_type=Page, file_path=standard_path)[0]
