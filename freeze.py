from markdown import Markdown
from flask_frozen import Freezer
from flask_app import app
from pathlib import Path
from glob import iglob

freezer = Freezer(app)

@freezer.register_generator
def posts():
    pages = iglob('content/*.md')
    for page in pages:
        p = Path(page)
        yield {'name': p.stem}

if __name__ == '__main__':
    freezer.freeze()
