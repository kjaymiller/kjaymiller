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

pageInfo = namedtuple('pageInfo', ['filename', 'contents'])
pageObject = namedtuple('pageObject', ['filename', 'page'])

detail_page = pageInfo('detailed_page', ''),
slug_page = pageInfo('slug_page', 'slug: slug_page_id\n\nThis is the slug Page.'),
id_page = pageInfo('id_page', 'id: id_page_id\n\nThis is the id Page.'),

def create_page(tmp_dir, page):
    filepath = tmp_dir.join(page[0].filename + '.md')
    filepath.write(page[0].contents)
    return pageObject(filepath, Page(base_file=Path(filepath)))

def test_no_empty_page(tmpdir):
    """An empty Page Item cannot be Created?"""
    empty_page = pageInfo('empty_page', ''),
    with pytest.raises(IndexError):
        create_page(tmpdir, empty_page)[-1]


title_page = pageInfo('page_with_title', 'title: The title of the Page\n\nThis is the Title Page.'),
no_title_page = pageInfo('page_with_title', 'This is the No Title Page.'),
@pytest.mark.parametrize('page,expected_title', (
                            (no_title_page, ''),
                            (title_page, 'The title of the Page'),
                            ))
def test_page_detects_title_or_empty(tmpdir, page, expected_title):
    """When Creating a Page item,
    both an id and title object are created"""
    test_page = create_page(tmpdir, page)[-1]
    assert test_page.metadata['title'] == expected_title


@pytest.mark.parametrize('page,expected_id', (
                            ('empty_page', 'empty_page'),
                            ('slug_page','slug_page_id'),
                            ('id_page', 'id_page_id'),
                            ))
def test_page_id_is_id_slug_or_stem(create_page, page, expected_id):
    """When Creating a Page item,
    the 'id' is one of three cases:
    1. the defined 'id'
    2. the defined 'slug'
    3. the stem of the file
    """
    test_page = create_page(standard_pages[page])
    assert test_page.metadata['id'] == expected_id


def test_page_summary(create_page):
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    summary_page = """title: Summary_page
    summary: this is a summary
    This is the content of the page.
    """

    pass
