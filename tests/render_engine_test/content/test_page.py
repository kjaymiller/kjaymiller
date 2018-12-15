"""
Tests the rendering of base page items and their subclasses.
 """ 
import pytest
from collections import namedtuple
from render_engine.content import Page
from pathlib import Path


pageInfo = namedtuple('pageInfo', ['filename', 'contents'])


@pytest.mark.parametrize('holder, optional_keys',(
    ({'foo':'bar'}, ()),
    ({'biz':'bar'}, ('biz')),
    ({'biz': 'bar'}, ['biz']),
    ({'zip': 'bar'}, ('biz', 'zip')),
    ({'biz': 'bar'}, {'biz'}),
    ))
def test_alt_keys(holder, optional_keys):
    """
    Tests all three cases of the alt_keys function.
    Case 1: expected_key is in holder
    Case 2: one of optional keys is in holder
    Case 3: neither the expected_key nor any of the optional keeys are in holder and the system_default must be used
    """
    from render_engine.content import alt_keys
    assert alt_keys(holder, optional_keys, 'bar') == 'bar' 


@pytest.fixture()
def create_page(tmpdir):
    pages = (
            pageInfo('empty_page', ''),
            pageInfo('detailed_page', ''),
            pageInfo('slug_page', 'slug: slug_page_id\n\nThis is the slug Page.'),
            pageInfo('id_page', 'id: id_page_id\n\nThis is the id Page.'),
            pageInfo('page_with_title', 'title: The title of the Page\n\nThis is the Title Page.'),
            )
    page_items = {}
    for page in pages:
        filepath = tmpdir.join(f'{page.filename}.md')
        filepath.write(page.contents)
        page_items[page.filename] = Page(base_file=Path(filepath))
    yield page_items


def test_new_page(create_page):
    """Can a Page Item Be Created?"""
    assert create_page['empty_page']  


@pytest.mark.parametrize('page,expected_title', (
                            ('empty_page', ''),
                            ('page_with_title', 'The title of the Page'),
                            ))
def test_page_detects_title_or_empty(create_page, page, expected_title):
    """When Creating a Page item, 
    both an id and title object are created"""
    test_page = create_page[page]
    assert test_page.metadata['title'] == expected_title


@pytest.mark.parametrize('page,key,expected_value', (
                            ('empty_page', 'id', 'empty_page'),
                            ('slug_page','id', 'slug_page_id'),
                            ('id_page', 'id', 'id_page_id'),
                            ))
def test_page_id_is_id_slug_or_stem(create_page, page, expected_id):
    """When Creating a Page item, 
    the 'id' is one of three cases:
    1. the defined 'id'
    2. the defined 'slug'
    3. the stem of the file
    """
    test_page = create_page[page]
    assert test_page.metadata['id'] == expected_id
