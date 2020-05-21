from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link


HEADER_LINKS = (
    Link(name='Blog', url='/all_blog_posts.html'),
    Link(name='MicroBlog', url='https://micro.blog/kjaymiller',
    icon='fab fa-microblog'),
    Link(name='Productivity in Tech', url='https://productivityintech.com'),
    Link(name='Contact', url='/contact', icon='fas fa-paper-plane'),
    Link(name='YouTube', url='https://www.youtube.com/channel/UCjoJU65IbXkKXsNqydro05Q'),
    Link(name='Twitch', url='https://twitch.tv/kjaymiller'),
    Link(name='Projects', url='/projects'),
    Link(name='Resume', url='/static/files/Jay_Miller_-_Software_Engineer.pdf'),
    )

mysite = Site(strict=True)
mysite.SITE_TITLE = 'Jay Miller'
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
class Projects(Collection):
    routes = ["", "projects"]
    content_path = "content/projects"
    template = "page.html"
    has_archive = True


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

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.microblog_posts = mysite.collections['MicroBlog'].pages[:5]
        self.blog_posts = mysite.collections['Blog'].pages[:5]


mysite.render(dry_run=False)
