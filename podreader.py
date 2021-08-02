import json
from pathlib import Path

import dateutil.parser as parser
import feedparser
import frontmatter
import pytz
from slugify import slugify


def download(podcast_name, podcast_data, from_date):
    """get episodes in rss feed, check against the from_date and add to content"""

    feed = feedparser.parse(podcast_data["feed_url"])
    tz = pytz.timezone("GMT")

    for entry in feed.entries:

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

        post = frontmatter.loads(f"{entry.content[0]['value']}")
        post.metadata.update(entry_data)
        post_content = frontmatter.dumps(post)
        Path("content", f"{slugify(filepath)}.md").write_text(post_content)


def main(json_file, section="active"):
    with open(json_file) as filepath:
        podcasts = json.load(filepath)

        for name, podcast in podcasts[section].items():
            print(f"processing {name}")
            from_date = podcast.get("from_date", "06 October 1989 12:00 GMT")
            download(
                podcast_name = name,
                podcast_data=podcast,
                from_date=from_date
            )


if __name__ == "__main__":
    main("content/podcasts.json")
    main("content/podcasts.json", section="retired")
