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

@pytest.fixture
def empty_page():
    return create_page('empty_page', '')
def test_no_empty_page(tmpdir):
    """An empty Page Item cannot be Created?"""
    with pytest.raises(IndexError):
        create_page(tmpdir, empty_page)

@pytest.fixture
def title_page(tmpdir):
    return create_page(tmpdir,
                       'page_with_title',
                       '''title: The title of the Page
                       This is the Title Page.''').title

@pytest.fixture
def no_title_page(tmpdir):
    no_title_page = create_page(tmpdir,
                                'page_no_title',
                                'This is the No Title Page.').title


@pytest.mark.parametrize('page,expected_title', (
                            (no_title_page, ''),
                            (title_page, 'The title of the Page'),
                            ))
def test_page_detects_title_or_empty(page, expected_title):
    """When Creating a Page item,
    both an id and title object are created"""
    assert page.title == expected_title


@pytest.fixture
def slug_page(tmpdir):
    id = create_page(tmpdir, 'slug_page',
                      'slug: slug_page_id\n\nThis is the slug Page.').id
    return id

@pytest.fixture
def id_page(tmpdir):
    id =  create_page(tmpdir, 'id_page',
                       'id: id_page_id\n\nThis is the id Page.').id
    return id
@pytest.mark.parametrize('page,expected_id', (
                            (slug_page,'slug_page_id'),
                            (id_page, 'id_page_id'),
                            ))
def test_page_id_is_id_slug_or_stem(page, expected_id):
    """When Creating a Page item,
    the 'id' is one of three cases:
    1. the defined 'id'
    2. the defined 'slug'
    3. the stem of the file
    """
    assert page() == expected_id


def test_page_summary():
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    summary_page = """title: Summary_page
    summary: this is a summary
    This is the content of the page.
    """

    pass
