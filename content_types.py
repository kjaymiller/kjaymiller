from pages import (
        Page,
        BlogPost,
        Collection,
        MicroBlogPost
        )

microblog = Collection(name='microblog', content_type=MicroBlogPost, content_path='microblog', output_path='microblog')
pages = Collection(name='pages', content_type=Page, content_path='pages')
projects = Collection(name='projects', content_type=Page, content_path='projects', output_path='projects')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')

CONTENT_TYPES = (pages, projects, blog) # removed microblog
CATEGORIZED = blog,
PAGINATION = blog,
