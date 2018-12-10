from collections import namedtuple
FREEZER_RELATIVE_URLS = True
FREEZER_DESTINATION = 'site'

SITE_TITLE = "K Jay Miller"
SITE_SUBTITLE = "The Corner of Automation, Productivity, and Community"
SITE_URL = "https://kjaymiller.com"
AUTHOR = 'KJAYMILLER'
REGION = 'US/Pacific'

# Header Links
Link = namedtuple('Link', ['title', 'href'])
HEADER_LINKS = (
    Link('Automations', '/blog/category/automation'),
    Link('Blog', '/blog_posts.html'),
    Link('Newsletter', '/subscribe.html'),
    Link('Contact','pages/contact.html'),
    Link('PIT', 'https://productivityintech.com'),
)
