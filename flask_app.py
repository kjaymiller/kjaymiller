from pathlib import Path
from flask import Flask, render_template
from flask_scss import Scss
from blog_engine.parse_markdown import JSON_Feed, Blog
from blog_engine.render_post import render_post
from urllib.parse import unquote
import json
import config
import string

app = Flask(__name__)
app.config.from_object('config')


pages = JSON_Feed('content/pages')

blog = Blog('content',
            json_base='blog_feed.json',
            json_filename='blog.json',
            json_title=config.SITE_TITLE)

micro = Blog('content/microblog',
             title=False,
             json_base='micro_feed.json',
             json_filename='micro.json',
             json_title=f'{config.SITE_TITLE} - Microblog')


feeds = {
        'pages': pages,
        'blog': blog,
        'micro': micro,
        }

@app.route("/")
def index():
    latest_post = blog.latest
    latest_micropost = micro.latest
    return render_template(
            'index.html',
            config=config,
            blog_object = blog.json_object,
            micro_object = micro.json_object,
            latest_post=latest_post,
            latest_micropost=latest_micropost,
            )


@app.route("/<JSON_FEED>/<slug>.html")
def post(JSON_FEED, slug):
    metadata = feeds[JSON_FEED].json_object[unquote(slug)]
    author = metadata.get('author', config.AUTHOR)
    return render_template(f'{JSON_FEED}.html', metadata = metadata)


@app.route("/<JSON_FEED>_posts.html")
def blog_posts(JSON_FEED):
    json_object = feeds[JSON_FEED].json_object
    sorted_list = sorted(json_object,
                         key=lambda x: json_object[x]['date_published'],
                         reverse=True)

    return render_template('blog_list.html',
                           title_list= sorted_list,
                           json_object = json_object,
    )
if __name__ == '__main__':
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(host='0.0.0.0', port=8000, debug=True)
