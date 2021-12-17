import pathlib
from datetime import datetime
import dateutil.parser as parser

import frontmatter
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from markdown2 import markdown

client = Elasticsearch(
    hosts=["jays-mac-mini-3.local"],
)

es_docs = []


def update_date(fparser):
    try:
        fparser['date'] = parser.parse(fparser['date'])

    except:
        pass

    try:
        fparser['tags'] = fparser['tags'].strip().split(',')

    except:
        pass
    return fparser


for path in pathlib.Path("content").iterdir():
    if not path.suffix == ".md":
        continue

    content = path.read_text()
    post = frontmatter.loads(content)

    if not post.metadata:
        print("ERROR!!")
        break

    attrs = {
        **post.metadata,
        **{"content": BeautifulSoup(markdown(post.content), "html.parser").text},
    }
    es_docs.append({k.lower(): v for k, v in attrs.items()})

es_docs = [update_date(doc) for doc in es_docs]

print("Uploading!")

bulk(client, es_docs, index="kjaymiller-test")
