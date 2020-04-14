import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link

# logging.basicConfig(level=logging.INFO)

HEADER_LINKS = (
    Link(name='Blog', url='/all_posts.html'),
    Link(name='MicroBlog', url='https://micro.blog/kjaymiller',
    icon='fab fa-microblog'),
    Link(name='Productivity in Tech', url='https://productivityintech.com'),
    Link(name='Contact', url='/contact', icon='fas fa-paper-plane'),
    Link(name='YouTube', url='https://www.youtube.com/channel/UCjoJU65IbXkKXsNqydro05Q'),
    Link(name='Twitch', url='https://twitch.tv/kjaymiller'),
    )

mysite = Site(strict=True)
mysite.SITE_TITLE = 'Jay Miller'
mysite.SITE_URL = 'https://kjaymiller.com'
mysite.HEADER_LINKS = HEADER_LINKS

@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"



@mysite.register_collection
class blog(Blog):
    routes = ['', '/blog']
    template = 'blog.html'
    subcollections = ['category', 'tags']

@mysite.register_collection
class microBlog(MicroBlog):
    routes = ['/microblog']
    template = 'blog.html'
    archive_template = 'microblog_archive.html'

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index.html"


mysite.render(dry_run=False)
