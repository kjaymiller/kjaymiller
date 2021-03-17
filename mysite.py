import json

from render_engine.links import Link
from render_engine.site import Site


def load_json(filename):
    with open(filename) as j:
        return json.load(j)


class MySite(Site):
    HEADER_LINKS = (
        Link(name="About", url="/about.html"),
        Link(name="Blog", url="/blog-0.html"),
        Link(name="Productivity", url="/productivity-0.html"),
        Link(name="Development", url="/development-0.html"),
        Link(name="Podcasts", url="/podcasts.html"),
        Link(name="Projects", url="/projects.html"),
        Link(name="Newsletter", url="/subscribe"),
        Link(name="Contact", url="/contact"),
    )
    timezone = "US/Pacific"
    SITE_TITLE = "Jay Miller"
    SITE_URL = "https://kjaymiller.com"
    AUTHOR = "Jay Miller"
    HEADER_LINKS = HEADER_LINKS
    SUBCOLLECTION_MIN = 2
    GUEST_APPEARANCES = load_json("content/guest-appearances.json")
    PROJECTS = load_json("content/projects.json")
    PODCASTS = load_json("content/podcasts.json")
    CONFERENCE_TALKS = load_json("content/conference-talks.json")
