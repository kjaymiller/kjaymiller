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
import json
import subprocess

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

SPONSORS_QUERY = """{
  viewer {
    sponsorshipsAsMaintainer(first: 100, activeOnly: true) {
      nodes {
        sponsorEntity {
          ... on User { login url }
          ... on Organization { login url }
        }
        tier { monthlyPriceInDollars }
      }
    }
  }
}"""


def get_sponsors():
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={SPONSORS_QUERY}"],
        capture_output=True,
        text=True,
    )
    data = json.loads(result.stdout)
    nodes = data["data"]["viewer"]["sponsorshipsAsMaintainer"]["nodes"]
    return [
        {"name": n["sponsorEntity"]["login"], "url": n["sponsorEntity"]["url"]}
        for n in nodes
    ]


if __name__ == "__main__":
    template = environment.get_template(".readme_template.md")
    Path("./readme.md").write_text(
        template.render(
            latest_microblog_post=latest_microblog_post,
            latest_conduit_episode=latest_conduit_episode,
            latest_blog_post=latest_post,
            sponsors=get_sponsors(),
        )
    )
