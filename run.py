import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link
from render_engine.search import Fuse



HEADER_LINKS = (
    Link(name='About', url='/about.html'),
    Link(name='Blog', url='/all_posts.html'),
    Link(name='Projects', url='/projects.html'),
    Link(name='Resume', url='/static/files/Jay_Miller_-_Software_Engineer.pdf'),
    Link(name='Newsletter', url='/subscribe'),
    )

mysite = Site(strict=True, timezone='US/Pacific')
mysite.SITE_TITLE = '(K) Jay Miller'
mysite.SITE_URL = 'https://kjaymiller.com'
mysite.AUTHOR = 'Jay Miller'
mysite.HEADER_LINKS = HEADER_LINKS
mysite.PODCASTS = [
        Link(
            name="Bob's Taverncast",
            url='https://bobstavern.pub',
            image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/bobstavern_256.jpg",
            ),
        Link(name="PIT Podcast", url='https://podcast.productivityintech.com',
            image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/pitpodcast_logo_256.jpg"),
        Link(name="TekTok Podcast", url='https://www.tekside.net/tektok',
            image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/tektok_256.jpeg"),
        ]
mysite.search = Fuse

@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ['', '/blog']
    template = 'blog.html'
    archive_template = 'archive.html'
    archive_slug = 'all_posts'
    content_path = 'content'
    subcollections = ['category', 'tags']
    paginated = True

@mysite.register_collection
class MicroBlog(MicroBlog):
    content_path = 'content/microblog'
    routes = ['/microblog']
    template = 'blog.html'
    archive_template = 'microblog_archive.html'
    archive_slug = 'all_microblog_posts'
    paginated = True

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index"
    no_index = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # logging.warning(mysite.collections['MicroBlog'].archive[0])
        # logging.warning(mysite.collections['Blog'].archive[0])
        self.microblog_posts = mysite.collections['MicroBlog'].archive[0].pages[:5]
        self.blog_posts = mysite.collections['Blog'].archive[0].pages[:5]

@mysite.register_route
class Categories(Page):
    template = "lists.html"
    slug = "categories"
    no_index = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # logging.warning(mysite.subcollections)
        self.list_section = mysite.subcollections['category']

mysite.render(dry_run=False)
