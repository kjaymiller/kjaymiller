from links import Link

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


HEADER_LINKS = (
    Link(name='Blog', url='/blog/blog_0.html'),
    Link(name='Newsletter', url='/subscribe.html'),
    Link('Contact','/contact.html'),
    Link('PIT', 'https://productivityintech.com'),
    Link('Podcasts', links=[
                        Link(name='Productivity in Tech Podcast', 
                            url='https://productivityintech.transistor.fm', 
                            image="https://s3-us-west-2.amazonaws.com/kjaymiller/images/pit-podcast.png"),
                        Link(name='Ask A Brit', 
                            url='https://askabrit.transistor.fm',
                            image='https://kjaymiller.s3-us-west-2.amazonaws.com/images/AskABritv4.png'),
                        Link('Dev Otaku', 'https://devotaku.transistor.fm')
                           ])
)
