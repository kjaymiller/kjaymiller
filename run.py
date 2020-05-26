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
    Link(name='Newsletter', url='https://buttondown.email/productivityintech'),
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
        Link(name="TekTok Podcast", url='https://www.tekside.net/tektok',
            image="https://images.squarespace-cdn.com/content/v1/511f025be4b09463c75fdc0e/1578770769608-WISTMD3GBO7J5FL34THW/ke17ZwdGBToddI8pDm48kNDA1KKPnejvrc8aNB1h53BZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PI_O0QXaCfy1WSgXfW7kCtZfhqU1lZMakzDgTpPIGZH6sKMshLAGzx4R3EDFOm1kBS/9AED1D17-64AB-4D39-A378-69B38D4A6BD9.jpeg?format=300w"),
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
