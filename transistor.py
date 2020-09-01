import os
import httpx
import typer
from pathlib import Path

header = {'x-api-key': os.environ.get('transistorKey')}
app = typer.Typer()

@app.command()
def get_show_list():
    url = 'https://api.transistor.fm/v1/shows'
    r = httpx.get(url, headers=header)
    typer.echo([(x['id'], x['attributes']['title']) for x in r.json()['data']])

@app.command()
def get_latest_episode( output: Path, show_id: int=799):
    episodes_url = 'https://api.transistor.fm/v1/episodes/'
    params = {"show_id": show_id}
    r = httpx.get(episodes_url, headers=header, params=params)
    episode = r.json()['data'][0]
    r = httpx.get(url=f"{episodes_url}:{episode}", headers=header)
    episode_attrs = episode['attributes']
    title = episode_attrs['title']
    published_date = episode_attrs['published_at']
    summary = episode_attrs['summary']
    embed_url = episode_attrs['embed_html']
    content = f"""title: {title}
    date: {published_date}
    {summary}
    {embed_url}"""
    output.write_text(content)


if __name__ == "__main__":
    app()
