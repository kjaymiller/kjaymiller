import os
from pathlib import Path

import httpx
import typer
from slugify import slugify

app = typer.Typer()

header = {"x-api-key": os.environ["transistorKey"]}


def get_show_list():
    """Get a list of all the shows"""

    url = "https://api.transistor.fm/v1/shows"
    r = httpx.get(url, headers=header)
    typer.echo([(x["id"], x["attributes"]["title"]) for x in r.json()["data"]])


@app.command()
def get_latest_episode(directory: Path, show_id: int = 799, episodes: int = 1):
    """Fetch the Latest Episode and write a render-engine template to the output"""

    episodes_url = "https://api.transistor.fm/v1/episodes/"
    params = {"show_id": show_id}
    r = httpx.get(episodes_url, headers=header, params=params)

    for episode in r.json()["data"][:episodes]:
        episode_attrs = episode["attributes"]
        title = episode_attrs["title"]
        output = directory.joinpath(slugify(title)).with_suffix(".md")

        if output.exists():
            return

        published_date = episode_attrs["published_at"]
        summary = episode_attrs["summary"]
        embed_url = episode_attrs["embed_html"]
        IMAGEKIT_PUBLIC_KEY = os.environ.get("IMAGEKIT_PUBLIC_KEY")
        image_url = (
            episode_attrs.get("image_url")
            or f"https://ik.imagekit.io//{IMAGEKIT_PUBLIC_KEY}/pit-logo-v5.jpg"
        )
        content = f"""title: {title}
date: {published_date}
image: {image_url}
tags: podcast
category: The PIT Show

{summary}
{embed_url}"""
        output.write_text(content)


if __name__ == "__main__":
    app()
