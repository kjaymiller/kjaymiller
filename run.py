import logging
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
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
mysite.SITE_TITLE = '(K)Jay Miller'
mysite.SITE_LINK = 'https://kjaymiller.com'
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
    template = "blog.html"

mysite.render(dry_run=False)
