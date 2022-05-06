from render_engine import Blog, Collection, Page
from render_engine.feeds import RSSFeed
from mysite import MySite

mysite = MySite(static='static')


@mysite.render_collection
class Pages(Collection):
    content_path = "content/pages"
    template = "page.html"

class Blog(Blog):
    template = "blog.html"
    feed = RSSFeed
    content_path = "content"
    archive_template = "blog_list.html"
    has_archive = True
    items_per_page = 10

# Running render separately to save pages to variable for Index's Featured Post
blog = mysite.render_collection(Blog)

@mysite.render_page
class Index(Page):
    template = "index.html"
    featured_post = blog.sorted_pages[0]
