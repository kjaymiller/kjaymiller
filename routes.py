from render_engine import Blog, Collection, Page
import pdb
import json
from mysite import MySite

mysite = MySite(static='static')

with open('content/podcasts.json') as podcast_file:
    podcasts = json.load(podcast_file)

with open('content/projects.json') as project_file:
    projects = json.load(project_file)

@mysite.render_collection
class Pages(Collection):
    content_path = "content/pages"
    template = "page.html"

class Blog(Blog):
    template = "blog.html"
    content_path = "content"
    archive_template = "blog_list.html"
    has_archive = "True"
    items_per_page = 10

blog = mysite.render_collection(Blog)

@mysite.render_page
class Index(Page):
    template = "index.html"
    slug = "index"
    featured_post = blog[0]
    podcasts = podcasts

@mysite.render_page
class Contact(Page):
    template = "contact.html"


@mysite.render_page
class podcasts(Page):
    template = "podcasts.html"
    podcasts = podcasts

@mysite.render_page
class Projects(Page):
    template = "projects.html"
    projects = projects
