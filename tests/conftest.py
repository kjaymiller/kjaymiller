import pytest
from render_engine.content import Page, BlogPost, MicroBlogPost

@pytest.fixture(scope="session")
def standard_path(tmp_path_factory):
    return tmp_path_factory.mktemp('test')


def create_file(standard_path, file_name, content):
    file_item = standard_path / file_name 
    with open (file_item, 'w') as f:
        f.write(content)
    return file_item


@pytest.fixture(scope="session")
def standard_file(standard_path):
    content = '''title:test item
this is a test file'''
    return create_file(standard_path, 'test_file.md', content)

@pytest.fixture(scope='session')
def standard_Page(standard_path):
    content = '''title: Standard Page
id: standard-page
date: December 19, 2018
This is a standard page with some metadata and some content.'''
    file_item = create_file(standard_path, 'standard_page.md', content)
    return Page(base_file=file_item)

@pytest.fixture(scope='session')
def standard_BlogPost(standard_path):
    content = '''title: Basic Blog Post\nThis is content for a blog post'''
    file_item = create_file(standard_path, 'standard_blog_post.md', content)
    return BlogPost(base_file=file_item)


@pytest.fixture(scope='session')
def complete_BlogPost(standard_path):
    content = '''title: Complete Blog Post
summary: This post has a custom summary
id: complete_blog_post
date: December 19, 2018
This is a more detailed blog post.'''
    file_item = create_file(standard_path, 'complete_blog_post.md', content)
    return BlogPost(base_file=file_item)

@pytest.fixture(scope='session')
def standard_MicroBlogPost(standard_path):
    content = '''This is a microblog post.'''
    file_item = create_file(standard_path, 'standard_microblog_post.md', content)
    return MicroBlogPost(base_file=file_item)
