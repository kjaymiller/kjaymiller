from render_engine.site import Site
from render_engine.links import Link

class MySite(Site):
    strict = True
    HEADER_LINKS = (
        Link(name="About", url="/about.html"),
        Link(name="Blog", url="/blog-0.html"),
        Link(name="Podcasts", url="/podcasts.html"),
        Link(name="Projects", url="/projects.html"),
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
