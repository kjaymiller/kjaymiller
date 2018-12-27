from render_engine.content import Page, BlogPost, MicroBlogPost
import pytest
from render_engine.generators import path_crawler
from pathlib import Path


def test_paths(standard_file, standard_path):
    assert len([a for a in standard_path.iterdir()]) == 1


@pytest.fixture(scope="session")
def path_types(standard_Page):
    item_types = (standard_Page, 
            standard_BlogPost, 
            standard_MicroBlogPost)

class TestPathCrawler():
    def test_path_crawler(self, standard_file, standard_path):
        assert path_crawler(item_type=Page, file_path=standard_path)

    def test_path_crawler_accepts_path_items(self,standard_file,  standard_path):
        assert path_crawler(item_type=Page, file_path=standard_path)[0]
