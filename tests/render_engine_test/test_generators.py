from render_engine.content import Page
import pytest
from render_engine.generators import path_crawler
from pathlib import Path


class TestPathCrawler():
    @pytest.fixture(scope="class")
    def standard_path(tmp_path_factory):
        return tmp_path_factory
    
    @pytest.fixture(scope="class")
    def standard_file(standard_path)
    with open (file_item, 'w') as f:
            f.write('title:test item\nthis is a test file')
        return file_item
    
    def test_path_crawler(self, standard_path):
        assert path_crawler(item_type=Page, file_path=self.standard_path.parent)

    def test_path_crawler_accepts_path_items(self, tmpdir):
        assert path_crawler(item_type=Page, file_path=self.standard_path.parent)[0]
