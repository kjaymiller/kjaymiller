"""
Tests the rendering of base page items and their subclasses.
 """
import pytest
from collections import namedtuple
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from pathlib import Path

class TestPage():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return Page(base_file=Path(filepath))

    @pytest.fixture(scope='class')
    def standard_page(self, tmpdir_factory):
        content = '''title: Standard Page
id: standard-page
date: December 19, 2018


This is a standard page with some metadata and some content.'''
        return self.create_entry(
                tmpdir_factory,
                'standard_page',
                content)

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
    def test_page_content_is_string(self, standard_page):
       assert standard_page.content == '''This is a standard page with some metadata and some content.'''

class TestBlogPost():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return BlogPost(base_file=Path(filepath))

    @pytest.fixture(scope='class')
    def basic_post(self, tmpdir_factory):
        basic_blog_post = '''title: Basic Blog Post\nThis is content for a blog post'''
        return self.create_entry(
                tmpdir_factory,
                'basic_post',
                basic_blog_post,
                )

    def test_blog_object(self, basic_post):
        assert basic_post

class TestPostSummary(TestBlogPost):
    """
    When a page is created, a summary can be generated using a summary tag.
    alternatively, it can also be created by calling__summary_from_title__
    """

    @pytest.fixture(scope='class')
    def summary_page(self, tmpdir_factory):
        summary_page = """title: Summary_page
summary: this is a summary
This is the content of the page."""
        return self.create_entry(tmpdir_factory, 'summary_page', summary_page)

    @pytest.fixture(scope='class')
    def no_summary_page(self, tmpdir_factory):
        no_summary_page = 'There is no summary on this page.'
        return self.create_entry(tmpdir_factory, 'no_summary_page', no_summary_page)

    def test_summary_from_page(self, summary_page):
        assert summary_page.summary == 'this is a summary...'

    def test_no_summary_from_page(self, no_summary_page):
        assert no_summary_page.summary == 'There is no summary on this page...'

class TestMicroBlog():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return MicroBlogPost(base_file=Path(filepath))

    @pytest.fixture(scope='class')
    def title_microblog(self, tmpdir_factory):
        content = '''This is a microblog post. It should have no title.'''
        return self.create_entry(tmpdir_factory, 'title_empty_microblog', content)

    def test_page_detects_title(self, title_microblog):
        """MicroBlogs have no title should always equal ''"""
        assert title_microblog.title == ''

class TestPodcastEpisode():
    def create_entry(self, tmpdir_factory, filename, contents):
        filepath = tmpdir_factory.mktemp('content').join(filename + '.md')
        filepath.write(contents)
        return PodcastEpisode(base_file=Path(filepath))
