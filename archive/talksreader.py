"""
Parse List of Conference Talks
"""
import json
from pathlib import Path
import frontmatter
from slugify import slugify

json_file = "content/conference-talks.json"

with open(json_file) as filepath:
    talks = json.load(filepath)

for entry in talks:
    file_title = slugify(f"{entry['title']} {entry['event']}")
    entry_data = {
        "title": entry['title'],
        "date": entry['last_presented'],
        "link": entry.get('link', ""),
        "tags": f"{entry['event']}, {entry.get('tags', '')}",
        "youtube": entry.get('embed', ""),
    }

    post = frontmatter.loads(f"{entry['abstract']}")
    post.metadata.update(entry_data)
    post_content = frontmatter.dumps(post)
    Path("content", f"{file_title}.md").write_text(post_content)
