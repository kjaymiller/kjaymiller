"""
Tests the rendering of base page items and their subclasses.
 """
import pytest
from collections import namedtuple
from render_engine.content import Page
from pathlib import Path


def create_page(tmpdir, filename, contents):
    filepath = tmpdir.join(filename + '.md')
    filepath.write(contents)
    return Page(base_file=Path(filepath))

def test_empty_page(tmpdir):
    with pytest.raises(IndexError):
        return create_page(tmpdir, 'empty_page', '')

@pytest.fixture
def title_page(tmpdir):
    return create_page(tmpdir,
           'page_with_title',
           '''title: The title of the Page
           This is  the Title Page.''')

@pytest.fixture
def no_title_page(tmpdir):
    return create_page(tmpdir,
            'page_no_title',
            'This is the No Title Page.')

def test_page_detects_title(title_page):
    """When Creating a Page item,
    both an id and title object are created"""
    assert title_page.title == 'The title of the Page'

def test_no_page_detects_title(no_title_page):
    """When Creating a Page item,
    both an id and title object are created"""
    assert no_title_page.title == ''


class TestIdProperty():
    @pytest.fixture
    def slug_page(self, tmpdir):
        id = create_page(tmpdir, 'slug_page',
                          'slug: slug_page_id\n\nThis is the slug Page.').id
        return id

    @pytest.fixture
    def id_page(self, tmpdir):
        id =  create_page(tmpdir, 'id_page',
                           'id: id_page_id\n\nThis is the id Page.').id
        return id

    @pytest.fixture
    def no_id_page(self, tmpdir):
        id =  create_page(tmpdir, 'no_id_page',
                           'This is the NO id Page.').id
        return id

    def test_page_pulls_slug_for_id(self, slug_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id'
        2. the defined 'slug'
        3. the stem of the file
         """
        assert slug_page == 'slug_page_id'

    def test_page_id_puls_id_from_file(self, id_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id'
        2. the defined 'slug'
        3. the stem of the file
         """
        assert id_page == 'id_page_id'

    def test_page_id_puls_from_stem(self, no_id_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id'
        2. the defined 'slug'
        3. the stem of the file
         """
        assert no_id_page == 'no_id_page'

class TestPost():
    def __init__(self):
        from render_engine.content import Blog

    def create_post(self, tmpdir, filename):
        filepath = tmpdir.join(filename + '.md')
        filepath.write(contents)
        return Blog(base_file=Path(filepath))

    @pytest.fixture
    def basic_post(self):
        basic_post = '''Title: Basic Blog Post
This is content for a blog post'''
        return self.create_post(tmpdir, 'basic_post', basic_blog_post)

    def test_blog_object(self, basic_post):
        assert basic_post

class TestPostSummary(TestPost):
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    @pytest.fixture
    def summary_page(self, tmpdir):
        summary_page = """title: Summary_page
summary: this is a summary
This is the content of the page."""
        return self.create_post(tmpdir, 'summary_page', summary_page)

    @pytest.fixture
    def no_summary_page(self, tmpdir):
        no_summary_page = 'There is no summary on this page.'
        return self.create_post(tmpdir, 'no_summary_page', no_summary_page)

    def test_summary_from_page(self, summary_page):
        assert summary_page.summary == 'this is a summary...'

    def test_no_summary_from_page(self, no_summary_page):
        assert no_summary_page.summary == 'There is no summary on this page...'


