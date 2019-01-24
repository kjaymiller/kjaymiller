from collections import namedtuple

SITE_TITLE = "K Jay Miller"
SITE_SUBTITLE = "The Corner of Automation, Productivity, and Community"
SITE_URL = "https://kjaymiller.com"
AUTHOR = 'KJAYMILLER'
AUTHOR_EMAIL = 'jay@kjaymiller.com'
AUTHOR_URL = 'https://kjaymiller.com'
AUTHOR_IMAGE = ''
REGION = 'US/Pacific'
TIME_FORMAT = 'MMMM DD, YYYY HH:MM'
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATH = 'static'
ICON = ''
FAVICON = ''
DEFAULT_POST_IMAGE = ''
DEFAULT_POST_BANNER = ''

# Header Links
Link = namedtuple('Link', ['title', 'href'])
HEADER_LINKS = (
    Link('Blog', '/blog_0.html'),
    Link('Newsletter', '/subscribe.html'),
    Link('Contact','/contact.html'),
    Link('PIT', 'https://productivityintech.com'),
)
