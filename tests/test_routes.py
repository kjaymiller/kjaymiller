from applitools.selenium import Target

def test_homepage(simplehttpserver, browser, eyes):
    """Test that the index template loads"""
    browser.get("http://localhost:8000/")
    eyes.check("Homepage", Target.window().fully())


def test_contact(browser, eyes):
    """Test the page template loads"""
    browser.get("http://localhost:8000/about")
    eyes.check("Page Template", Target.window().fully())


def test_blog_archive(browser, eyes):
    """Test the blog archive template loads"""
    browser.get("http://localhost:8000/blog/blog-0")
    eyes.check("Blog Archive", Target.window().fully())


def test_blog_post(browser, eyes):
    """Test the blog post template loads"""
    browser.get(
        "http://localhost:8000/blog/make-inlay-type-hints-in-python-appear-disappear.html"
    )
    eyes.check("Blog Post", Target.window().fully())
