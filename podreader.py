import json
from pathlib import Path

import dateutil.parser as parser
import episode_dl
import frontmatter
import pytz
from rich import print
from slugify import slugify

tz = pytz.timezone("GMT")

def build_fmatter(entry_data: dict[str], content) -> bytes:
    """builds frontmatter based on the given data"""
    post = frontmatter.loads(content)
    post.metadata.update(entry_data)
    post_content = frontmatter.dumps(post)
    print("Building episode [orange bold] {post.metadata.title}")
    return Path("content", f"{slugify(filepath)}.md").write_text(post_content)

def download(podcast_name, podcast_data, from_date):
    """get episodes in rss feed, check against the from_date and add to
    content"""


    for entry in feed.entries:
        print(f"{entry=}")

        # Check episode published after from_date
        check_date = parser.parse(entry.published)

        if not check_date.tzinfo:
            check_date = tz.localize(check_date)

        if parser.parse(from_date) >= check_date:
            continue

        # Check podcast_name not in episode title
        if podcast_name not in entry.title:
            filepath = f"{podcast_name} - {entry.title}"

        else:
            filepath = entry.title

        entry_data = {
            "category": podcast_name,
            "title": entry.title,
            "slug": slugify(filepath),
            "date": entry.published,
            "link": entry.link,
            "image": podcast_data["image"],
        }

        yield build_fmatter(entry_data, entry.content[0]['value'])



def main(json_file, section="active"):
    with open(json_file) as filepath:
        podcasts = json.load(filepath)

        for name, podcast in podcasts[section].items():
            print(f"processing [bold blue] {name}")
            from_date = podcast.get("from_date", "06 October 1989 12:00 GMT")
            feed = feedparser.parse(podcast["feed_url"])
            download(
                podcast_name = name,
                podcast_data=podcast,
                from_date=from_date
            )


if __name__ == "__main__":
    main("content/podcasts.json")
#    main("content/podcasts.json", section="retired")
