from render_engine.content import Page
import generators

generators.generate()

pages = path(
        name = 'pages',
        content_type = Page,
        content_path = Path(f'{config.CONTENT_PATH}/pages'),
        output_path = Path(f'{config.OUTPUT_PATH}'/pages'),
        )

blog = path(
        name = 'blog',
        content_type = BlogPost,
        content_path = Path('content'),
        output_path = Path('blog'),
        )

microblog = path(
        name = 'microblog',
        content_type = MicroBlogPost,
        content_path = Path('content/microblog'),
        output_path = Path('microblog'),
        )

podcast = path(
        name = 'podcast',
        content_type = PodcastEpisode,
        content_path = Path('content/podcast'),
        output_path = Path('podcast'),
        )

PATHS = (pages, blog, podcast, microblog)
def index():
    page =  Page(template='index.html').html
    return generators.write_page('index', page)
index()
