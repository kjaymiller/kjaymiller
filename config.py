from dataclasses import dataclass

SITE_TITLE = "K Jay Miller"
SITE_SUBTITLE = "On the Corner of Automation, Productivity, and Community"
SITE_URL = "https://kjaymiller.com"
AUTHOR = 'KJAYMILLER'
AUTHOR_EMAIL = 'jay@kjaymiller.com'
AUTHOR_URL = 'https://kjaymiller.com'
AUTHOR_IMAGE = ''
REGION = 'US/Pacific'
TIME_FORMAT = 'MMMM DD, YYYY HH:mm'
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATH = 'static'
ICON = ''
FAVICON = ''
DEFAULT_POST_IMAGE = ''
DEFAULT_POST_BANNER = ''

# Header Links
class Link:
    def __init__(self, name, url='', links=[]):
        self.name = name
        self.url = url
        self.links = links

HEADER_LINKS = (
    Link('Blog', '/blog/blog_0.html'),
    Link('Newsletter', '/subscribe.html'),
    Link('Contact','/contact.html'),
    Link('PIT', 'https://productivityintech.com'),
    Link('Podcasts', links=[Link('Prodyctivity in Tech Podcast', 'https://productivityintech.transistor.fm'),
                           Link('Ask A Brit', 'https://askabrit.transistor.fm'),
                           Link('Dev Otaku', 'https://devotaku.transistor.fm')
                           ])
)
