import json
from pathlib import Path

import dateutil.parser as parser
import feedparser
import frontmatter
import pytz
from slugify import slugify


def download(url, show_title, from_date):
    feed = feedparser.parse(url)
    tz = pytz.timezone("GMT")

    for entry in feed.entries:
        check_date = parser.parse(entry.published)

        if not check_date.tzinfo:
            check_date = tz.localize(check_date)

        if parser.parse(from_date) >= check_date:
            continue

        if show_title not in entry.title:
            filepath = f"{show_title} - {entry.title}"
        else:
            filepath = entry.title

        entry_data = {
            "category": show_title,
            "title": entry.title,
            "slug": slugify(filepath),
            "date": entry.published,
            "link": entry.link,
        }

        post = frontmatter.loads(f"{entry.content[0]['value']}")
        post.metadata.update(entry_data)
        Path("content", f"{slugify(filepath)}.md").write_text(frontmatter.dumps(post))


def main(json_file):
    with open(json_file) as filepath:
        podcasts = json.load(filepath)

        for name, podcast in podcasts["active"].items():
            from_date = podcast.get("from_date", "06 October 1989 12:00 GMT")
            download(podcast["feed_url"], name, from_date)


if __name__ == "__main__":
    main("content/podcasts.json")
