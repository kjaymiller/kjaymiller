import feedparser
from pathlib import Path
from jinja2 import Template


def get_latest_post(rss_feed):
    f = feedparser.parse(rss_feed)
    latest_post = sorted(f['entries'], key=lambda x:x['published_parsed'])[-1]
    return {
            'title': latest_post['title'],
            'link': latest_post['link'],
            }

# update readme
if __name__ == '__main__':
    rss_feed = './output/blog.rss.xml'
    podcast_url = 'https://relay.fm/conduit/feed'
    template = Template(Path('./README_template.md').read_text())
    Path('./README.md').write_text(
            template.render(
                latest_post=get_latest_post(rss_feed),
                latest_podcast_post=get_latest_post(podcast_url),
                )
            )
