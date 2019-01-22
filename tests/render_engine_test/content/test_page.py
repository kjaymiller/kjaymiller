"""
Tests the rendering of base page items and their subclasses.
 """
import pytest
import arrow
from collections import namedtuple
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from pathlib import Path

class TestPage():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return Page(base_file=Path(filepath))


class TestPageTitle(TestPage):
    @pytest.fixture(scope='class')
    def title_page(self, tmpdir_factory):
        return self.create_entry(
                tmpdir_factory,
                'page_with_title',
                '''title: The title of the Page
                This is  the Title Page.''')

    @pytest.fixture(scope='class')
    def no_title_page(self, tmpdir_factory):
        return self.create_entry(
                tmpdir_factory,
                'page_no_title',
                'This is the No Title Page.')

    def test_page_detects_title(self, title_page):
        """When Creating a Page item,
        both an id and title object are created"""
        assert title_page.title == 'The title of the Page'

    def test_no_page_detects_title(self, no_title_page):
        """When Creating a Page item,
        both an id and title object are created"""
        assert no_title_page.title == ''


class TestIdProperty(TestPage):
    @pytest.fixture(scope='class')
    def slug_page(self, tmpdir_factory):
        return self.create_entry(
                tmpdir_factory, 
                'slug_page',
                'slug: slug_page_id\n\nThis is the slug Page.',
                )

    @pytest.fixture(scope='class')
    def id_page(self, tmpdir_factory): 
        return self.create_entry(
                tmpdir_factory, 
                'id_page',           
                'id: id_page_id\n\nThis is the id Page.',
                )

    @pytest.fixture(scope='class')
    def no_id_page(self, tmpdir_factory):
        return self.create_entry(
                tmpdir_factory, 
                'no_id_page',
                'This is the NO id Page.',
                )

    def test_page_pulls_slug_for_id(self, slug_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id'
        2. the defined 'slug'
        3. the stem of the file
         """
        assert slug_page.id== 'slug_page_id' 

    def test_page_id_puls_id_from_file(self, id_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id'
        2. the defined 'slug'
        3. the stem of the file
         """
        assert id_page.id == 'id_page_id'

    def test_page_id_puls_from_stem(self, no_id_page):
        """When Creating a Page item,
        the 'id' is one of three cases:
        1. the defined 'id' 
        2. the defined 'slug'
        3. the stem of the file 
         """
        assert no_id_page.id == 'no_id_page'


class TestPageContent(TestPage):
    def test_page_content_is_string(self, standard_path, standard_Page):
       assert standard_Page.content == '''This is a standard page with some metadata and some content.'''

class TestBlogPost():
    def test_blog_object(self, standard_BlogPost):
        assert standard_BlogPost

class TestPostSummary(TestBlogPost):
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    @pytest.mark.skip(reason='Upcoming Feature will correct')
    def test_summary_from_page(self, complete_BlogPost):
        summary_page = complete_BlogPost
        assert summary_page.summary == 'This post has a custom summary...'

    def test_no_summary_from_page(self, standard_BlogPost):
        no_summary_page = standard_BlogPost
        assert no_summary_page.summary


class TestBlogPostDate_Published():
    def test_date_exist(self, complete_BlogPost):
        assert complete_BlogPost.date_published
    
class TestMicroBlog():
    def test_page_detects_title(self, standard_MicroBlogPost):
        """MicroBlogs have no title should always equal ''"""
        assert standard_MicroBlogPost.title == ''

class TestPodcastEpisode():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return PodcastEpisode(base_file=Path(filepath))
