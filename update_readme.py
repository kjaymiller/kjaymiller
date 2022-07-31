from jinja2 import Environment, FileSystemLoader
from episode_dl import get_episodes
from pathlib import Path
import feedparser
environment = Environment(loader=FileSystemLoader('.'))


if __name__ == "__main__":
    latest_episode = get_episodes('https://www.relay.fm/conduit/feed')[0]
    template = environment.get_template('.readme_template.md')    
    # latest_post = sorted(feedparser.parse('jay-miller-blog.rss').entries, key= lambda x: x.published_parsed, reverse=True)[0]
    
    Path('./readme.md').write_text(template.render(
            latest_podcast_post=latest_episode,
            latest_blog_post=latest_post,
            )
    )
