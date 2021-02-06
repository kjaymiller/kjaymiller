import json
from render_engine import Collection, Blog, Page
from render_engine.links import Link
from render_engine.microblog import MicroBlog
from mysite import MySite

mysite = MySite()

@mysite.register_collection
class Pages(Collection):
    routes = ["", "pages"]
    content_path = "content/pages"
    template = "page.html"


@mysite.register_collection
class Blog(Blog):
    routes = ["", "/blog"]
    template = "blog.html"
    archive_template = "blog_list.html"
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
        self.microblog_posts = mysite.collections["MicroBlog"].archive[0].pages[:2]
        self.blog_posts = mysite.collections["Blog"].archive[0].pages[:1]


@mysite.register_route
class Contact(Page):
    template = "contact.html"
    slug = "contact"

@mysite.register_route
class Talks(Page):
    template = "conference-talks.html"
    slug = "conference-talks"
    talks = "Conference Talks"

    with open('content/conference-talks.json') as j:
        posts = json.load(j)

@mysite.register_route
class projects(Page):
    template = "projects.html"
    slug = "projects"
    title = "Projects"

    with open('content/projects.json') as j:
        posts = json.load(j)


@mysite.register_route
class podcast(Page):
    template = "podcasts.html"
    slug = "podcasts"
    title = "Podcasts"

    with open('content/guest-appearances.json') as j:
        posts = json.load(j)

