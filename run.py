import logging
import pendulum
from render_engine import Site, Page, Collection
from render_engine.microblog import MicroBlog
from render_engine.blog import Blog
from render_engine.links import Link

# logging.basicConfig(level=logging.INFO)

HEADER_LINKS = (
    Link(name='Blog', url='/all_posts.html'),
    Link(name='MicroBlog', url='/all_microblog_posts.html'),
    Link(name='Newsletter', url='https://buttondown.email/productivityintech'),
    Link(name='Productivity in Tech', url='https://productivityintech.com'),
    Link(name='Contact', url='/contact'),
    Link(name='Podcasts', url='/podcasts.html'),
    Link(name='GitHub', url='https://github.com/kjaymiller'),
    Link(name='YouTube', url='https://www.youtube.com/channel/UCjoJU65IbXkKXsNqydro05Q'),
    )

mysite = Site(strict=True)
mysite.SITE_TITLE = '(K)Jay Miller'
mysite.SITE_LINK = 'https://kjaymiller.com'
mysite.HEADER_LINKS = HEADER_LINKS

@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ['', '/blog']
    template = "blog.html"

@mysite.register_collection
class MicroBlog(MicroBlog):
    routes = ['/microblog']
    template = "blog.html"
    content_path = "content/microblog"

@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.posts = list(
                sorted(
                    mysite.collections['Blog'].pages,
                    key=lambda x:x.date,
                    reverse=True)
            )[:4]

        self.microblog_posts = list(
                sorted(
                    mysite.collections['MicroBlog'].pages,
                    key=lambda x:x.date,
                    reverse=True)
                )[:5]


mysite.render(dry_run=False)
