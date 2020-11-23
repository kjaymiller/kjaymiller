import os
import httpx
import typer
from slugify import slugify
from pathlib import Path


header = {'x-api-key': os.environ.get('transistorKey')}

def get_show_list():
    """Get a list of all the shows"""

    url = 'https://api.transistor.fm/v1/shows'
    r = httpx.get(url, headers=header)
    typer.echo([(x['id'], x['attributes']['title']) for x in r.json()['data']])

def get_latest_episode(directory: Path, show_id: int=799, episodes: int=1):
    """Fetch the Latest Episode and write a render-engine template to the output"""

    episodes_url = 'https://api.transistor.fm/v1/episodes/'
    params = {"show_id": show_id}
    r = httpx.get(episodes_url, headers=header, params=params)

    for episode in r.json()['data'][:episodes]:
        episode_attrs = episode['attributes']
        title = episode_attrs['title']
        published_date = episode_attrs['published_at']
        summary = episode_attrs['summary']
        embed_url = episode_attrs['embed_html']
        image_url = episode_attrs.get('image_url') or f'https://imagekit.io/{IMAGEKIT_PUBLIC_KEY}/pit-logo-v5.jpg'
        content = f"""title: {title}
date: {published_date}
image: {image_url}

{summary}
{embed_url}"""
        output = directory.joinpath(slugify(title)).with_suffix(".md")
        output.write_text(content)


if __name__ == "__main__":
    typer.run(get_latest_episode)
