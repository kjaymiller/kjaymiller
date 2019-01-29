from pages.blog import BlogPost


class MicroBlogPost(BlogPost):
    title = ''
    def __init__(self, base_file):
        super().__init__(base_file)

