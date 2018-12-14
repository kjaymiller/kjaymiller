"""
Tests the rendering of base page items and their subclasses.
 """ 
import pytest
import tempfile

@pytest.fixture()
def create_pages():
    pages_dir = tempfile.mkdtemp()
    pages = (
            ('empty_page', ''),
            ('detailed_page',''),
            ('slug_page','slug: slug_page_id'),
            ('id_page', 'id: id_page_id'),
            )
    for page in pages:
        with open(f'{pages_dir}/{page[0]}.md', 'w') as f:
            f.write(page[1])

@pytest.mark.userfixtures('create_pages')
class Test_Pages():
    def __init__(self,)
        from render_engine.content import Page
        from pathlib import Path

    def create_page(filename): 
        self.file_path = Path('tests/test_content/' + filename)
        self.new_page = Page(base_file=self.file_path)

    def empty_page(self):
        return NewPage(filename='').new_page

    @pytest.fixture(scope='module')
    def detailed_page():
        return NewPage(filename='detailed_page.md').new_page

    @pytest.fixture(scope='module')
    def slug_page():
        return NewPage(filename='slug_page.md').new_page

    def test_new_page(empty_page):
        """Can a Page Item Be Created?"""
        assert empty_page  

    def test_page_with_required_keys(empty_page):
        """When Creating a Page item, 
        both an id and title object are created"""
            
        assert empty_page.metadata['id']
        assert any((empty_page.metadata['title'], empty_page.metadata['title']==''))

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

