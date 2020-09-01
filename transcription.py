import typer
from pathlib import Path
from transcriptor.amazon import AmazonJob

app = typer.Typer()

@app.command()
def upload_file(filepath: str):
    job = AmazonJob(filepath=filepath, bucket='pit-transcriptions')
    job.start()

@app.command()
def build_file(filepath: str, output_file: Path):
    job = AmazonJob(filepath=filepath, bucket='pit-transcriptions', status='foo')

    if job.status == 'COMPLETED':
        job.build()
        output_file.write_text(job.transcript)

    else:
        typer.echo(job.status)

if __name__ == "__main__":
    app()
