"""
Tests the rendering of base page items and their subclasses.
 """ 
import pytest
from render_engine.content import Page
from pathlib import Path

def create_page(filename, contents):
    filepath = tmpdir.join(f'{page}.md')
    filepath.write(contents)
    return Page(base_file=filepath)

@pytest.yield_fixture()
def page(): 
    pages = {
        'empty_page': create_page('empty_page', ''),
        'detailed_page': create_page('detailed_page', ''),
        'slug_page': create_page('slug_page', 'slug: slug_page_id'),
        'id_page': create_page('id_page', 'id: id_page_id'),
        }

    yield page


def test_new_page(page):
    """Can a Page Item Be Created?"""
    assert page['empty_page']  

def test_page_with_required_keys(empty_page):
    """When Creating a Page item, 
    both an id and title object are created"""
        
    assert page['empty_page'].metadata['id']
    assert any((page['empty_page'].metadata['title'], empty_page.metadata['title']==''))

def test_page_id_is_stem(empty_page):
    """When Creating a Page item, 
    the 'id' of the item is the stem of the filename.
    """
    assert empty_page.metadata['id'] == NewPage('empty_page.md').file_path.stem

def test_page_with_id_or_slug_in_file(id_page, slug_page):
    """When Creating a Page item, 
    If there is an 'id' or 'slug' in the metadata,
    the 'id' of the item is the 'id' or 'slug' of the filename.
    """
        
    assert id_page.metadata['id'] == 'id_page_id'
    assert slug_page.metadata['slug'] == 'slug_plag_id'

