from gazpacho import Soup
import httpx
import pathlib

files = pathlib.Path('output').glob("*.html")

def check_against(href):
    checks = [
            'kjaymiller.com',
            'googleplaymusic',
            'linkedin.com/in/',
            ]

    for check in checks:
        if check in href:
            return False

    return True

for doc in files:
    html = Soup(doc.read_text())
    urls = html.find("a")

    for url in urls:
        href = url.attrs['href']

        if all([check_against(href), href.startswith('http')]): 
            try: 
                if (status := httpx.get(href).status_code) not in (304, 200):
                    print(doc.name, href, status)

            except Exception as e: 
                print(doc.name, href, e)

