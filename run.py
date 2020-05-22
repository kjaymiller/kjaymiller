import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link


HEADER_LINKS = (
    Link(name='About', url='/about.html'),
    Link(name='Blog', url='/all_posts.html'),
    Link(name='Projects', url='/projects.html'),
    Link(name='Productivity in Tech', url='https://productivityintech.com'),
    Link(name='MicroBlog', url='https://micro.blog/kjaymiller',
    icon='fab fa-microblog'),
    Link(name='Twitch', url='https://twitch.tv/kjaymiller', icon='fab fa-twitch'),
    Link(
        name="Github",
        url="https://github.com/kjaymiller",
        icon='fab fa-github'),
    Link(name='Resume', url='/static/files/Jay_Miller_-_Software_Engineer.pdf'),
    )

mysite = Site(strict=True)
mysite.SITE_TITLE = '(K) Jay Miller'
mysite.SITE_URL = 'https://kjaymiller.com'
mysite.HEADER_LINKS = HEADER_LINKS
mysite.PODCASTS = [
        Link(
            name="Bob's Taverncast",
            url='https://bobstavern.pub',
            image="https://images-internal.transistor.fm/images/show/5833/medium_1574279200-artwork.jpg",
            ),
        Link(name="PIT Podcast", url='https://podcast.productivityintech.com',
            image="https://images-internal.transistor.fm/images/show/799/medium_1561758687-artwork.jpg"),
        ]

@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ['', '/blog']
    template = 'blog.html'
    subcollections = ['category', 'tags']

@mysite.register_collection
class MicroBlog(MicroBlog):
    content_path = 'content/microblog'
    routes = ['/microblog']
    template = 'blog.html'
    archive_template = 'microblog_archive.html'
    archive_slug = 'all_microblog_posts'

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.microblog_posts = mysite.collections['MicroBlog'].archive.pages[:5]
        self.blog_posts = mysite.collections['Blog'].archive.pages[:5]


mysite.render(dry_run=False)
