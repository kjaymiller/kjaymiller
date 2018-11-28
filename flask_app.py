from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, Markup
from flask_scss import Scss
from blog_engine.parse_markdown import render_post, JSON_Feed
import json
import config

app = Flask(__name__)
app.config.from_object('config')

blog = JSON_Feed('blog_feed.json', Path('content'), new=True)

@app.route("/")
def index():
    return render_template('index.html', config=config)


@app.route("/blog/<slug>.html")
def blog_post(slug):
    filename = f'content/{blog.slug_table[slug]}'
    with open(filename) as f:
        metadata = render_post(f.read())
    post_content = Markup(metadata['content'])
    title = metadata['title']
    created_time = metadata.get('date', datetime.fromtimestamp(Path(filename).stat().st_ctime).strftime("%Y-%m-%d"))
    author = metadata.get('author', config.AUTHOR)
    return render_template('blog.html', 
            content = post_content,
            title = title,
            author = author,
            created = created_time)


@app.route("/blog_posts.html")
def blog_posts():
    return render_template('blog_list.html', title_list=blog.json_object['items'])


if __name__ == '__main__':
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(host='0.0.0.0', port=8000, debug=True)
