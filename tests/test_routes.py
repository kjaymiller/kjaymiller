import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

def test_homepage(browser):
    """Test that the homepage loads"""
    browser.get("https://kjaymiller.com")

def test_blog_archive(browser):
    """Test the blog archive loads"""
    browser.get("https://kjaymiller.com/blog/blog-0")
