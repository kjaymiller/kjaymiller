from pathlib import Path
from render_engine.content import Page
from flask import Flask, render_template, Response
from flask_scss import Scss
from urllib.parse import unquote
import json
import config
import string


app = Flask(__name__)
app.config.from_object('config')


""""
@app.route("/<feed>.json")
def generate_json_feed(feed):
    json_feed = feeds[feed].create_feed()
    return json.dumps(json_feed), 200, {'content-type':'application/json'}
"""
@app.route("/")
def index():
    return render_template(
            'index.html',
            config=config,
            # latest_posts=blog.sorted_items(2),
            # latest_micropost=micro.sorted_items(3),
            )


@app.route("/<path>/<id>.html")
def post(path, id, content, file_item):
    content = content
    file_item = file_item
    if path == Page:
        return render_template('pages.html', metadata=file_item )
    else:
        return render_template('post.html', file_item = file_item)
"""
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
"""

if __name__ == '__main__':
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(host='0.0.0.0', port=8000, debug=True)
