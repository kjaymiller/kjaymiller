import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link

# logging.basicConfig(level=logging.INFO)

HEADER_LINKS = (
    Link(name='Blog', url='/all_posts.html'),
    Link(name='MicroBlog', url='https://micro.blog/kjaymiller'),
    Link(name='Newsletter', url='/newsletter'),
    Link(name='Productivity in Tech', url='https://productivityintech.com'),
    Link(name='Contact', url='/contact'),
    Link(name='YouTube', url='https://www.youtube.com/channel/UCjoJU65IbXkKXsNqydro05Q'),
    )

mysite = Site(strict=True)
mysite.SITE_TITLE = 'Jay Miller'
mysite.SITE_URL = 'https://kjaymiller.com'
mysite.HEADER_LINKS = HEADER_LINKS

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index.html"


@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ['', '/blog']
    template = 'archive.html'
    subcollections = ['category', 'tags']

@mysite.register_collection
class MicroBlog(MicroBlog):
    routes = ['/microblog']
    template = 'archive.html'


print([x.slug for x in mysite.routes])
mysite.render(dry_run=False)
