"""
Tests the rendering of base page items and their subclasses.
 """
import pytest
from collections import namedtuple
from render_engine.content import Page
from pathlib import Path


@pytest.mark.parametrize('holder, optional_keys',(
    ({'foo':'bar'}, ()),
    ({'biz':'bar'}, ('biz')),
    ({'biz': 'bar'}, ['biz']),
    ({'zip': 'bar'}, ('biz', 'zip')),
    ({'biz': 'bar'}, {'biz'}),
    ))


def create_page(tmpdir, filename, contents):
    filepath = tmpdir.join(filename + '.md')
    filepath.write(contents)
    return Page(base_file=Path(filepath))

def test_empty_page(tmpdir):
    with pytest.raises(IndexError):
        return create_page(tmpdir, 'empty_page', '')

@pytest.fixture
def title_page(tmpdir):
    title_page = create_page(tmpdir,
                       'page_with_title',
                       '''title: The title of the Page
                       This is  the Title Page.''').title
    return title_page

@pytest.fixture
def no_title_page(tmpdir):
    no_title_page = create_page(tmpdir,
                                'page_no_title',
                                'This is the No Title Page.').title
    return no_title_page

def test_page_detects_title(title_page):
    """When Creating a Page item,
    both an id and title object are created"""
    assert title_page == 'The title of the Page'

def test_no_page_detects_title(no_title_page):
    """When Creating a Page item,
    both an id and title object are created"""
    assert no_title_page == ''


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

class TestPageSummaries():
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    @pytest.fixture
    def summary_page(self, tmpdir):
        summary_page = """title: Summary_page
summary: this is a summary
This is the content of the page."""
        return create_page(tmpdir, 'summary_page', summary_page).summary

    @pytest.fixture
    def no_summary_page(self, tmpdir):
        no_summary_page = 'There is no summary on this page.'
        return create_page(tmpdir, 'no_summary_page', no_summary_page).summary

    def test_summary_from_page(self, summary_page):
        assert summary_page == 'this is a summary...'

    def test_no_summary_from_page(self, no_summary_page):
        assert no_summary_page == 'There is no summary on this page...'
