import feedparser
import logging
import os
from render_engine import Site, Page, Collection
from render_engine.blog import Blog
from render_engine.microblog import MicroBlog
from render_engine.links import Link

class site(Site):
    strict = True
    HEADER_LINKS = (
        Link(name="About", url="/about.html"),
        Link(name="Blog", url="/blog-0.html"),
        Link(name="Projects", url="/projects.html"),
        Link(name="Resume", url="/static/files/Jay_Miller_-_Software_Engineer.pdf"),
        Link(name="Newsletter", url="/subscribe"),
        Link(name="Contact", url="/contact"),
    )

    timezone = "US/Pacific"
    SITE_TITLE = "(K) Jay Miller"
    SITE_URL = "https://kjaymiller.com"
    AUTHOR = "Jay Miller"
    HEADER_LINKS = HEADER_LINKS
    PODCASTS = [
        Link(
            name="Bob's Taverncast",
            url="https://bobstavern.pub",
            image="/bobstavern_256.jpg",
        ),
        Link(
            name="The PIT Show",
            url="https://podcast.productivityintech.com",
            image="/pit-logo-v5.jpg",
        ),
        Link(
            name="TekTok Podcast",
            url="https://www.tekside.net/tektok",
            image="/tektok_256.jpeg",
        ),
        Link(
            name="Ask a Brit",
            url="https://askabrit.transistor.fm",
            image="/AskABritv4.png",
        ),
    ]


mysite = site()


@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ["", "/blog"]
    template = "blog.html"
    archive_template = "_archive.html"
    archive_slug = "all_posts"
    content_path = "content"
    subcollections = ["category", "tags"]
    paginated = True


@mysite.register_collection
class MicroBlog(MicroBlog):
    content_path = "content/microblog"
    routes = ["/microblog"]
    template = "blog.html"
    archive_template = "microblog_archive.html"
    archive_slug = "all_microblog_posts"
    paginated = True


@mysite.register_route
class Index(Page):
    template = "index.html"
    slug = "index"
    no_index = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.microblog_posts = mysite.collections["MicroBlog"].archive[0].pages[:5]
        self.blog_posts = mysite.collections["Blog"].archive[0].pages[:5]


@mysite.register_route
class contact(Page):
    template = "contact.html"
    slug = "contact"
    title = "Chat"


if __name__ == "__main__":
    mysite.render(dry_run=False)
    
