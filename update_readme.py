# /// script
# dependencies = [
#   "jinja2",
#   "episode_dl",
#   "feedparser",
# ]
# ///

from jinja2 import Environment, FileSystemLoader
from episode_dl import get_episodes
from pathlib import Path
import feedparser

environment = Environment(loader=FileSystemLoader("."))

MICROBLOG = "https://kjaymiller.com/microblog.rss"
CONDUIT_FEED = "https://www.relay.fm/conduit/feed"
BLOG_FEED = "https://kjaymiller.com/blog.rss"

latest_conduit_episode = get_episodes(CONDUIT_FEED)[0]
latest_microblog_post = sorted(
    feedparser.parse(MICROBLOG).entries,
    key=lambda x: x.published_parsed,
    reverse=True,
)[0]
latest_post = sorted(
    feedparser.parse(BLOG_FEED).entries,
    key=lambda x: x.published_parsed,
    reverse=True,
)[0]

if __name__ == "__main__":
    template = environment.get_template(".readme_template.md")
    Path("./readme.md").write_text(
        template.render(
            latest_microblog_post=latest_microblog_post,
            latest_conduit_episode=latest_conduit_episode,
            latest_blog_post=latest_post,
        )
    )
