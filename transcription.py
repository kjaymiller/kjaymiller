import typer
from pathlib import Path
from transcriptor.amazon import AmazonJob

app = typer.Typer()


@app.command()
def upload_file(filepath: str, speakers: int=0):
    job = AmazonJob(filepath=filepath, bucket='pit-transcriptions')

    if speakers > 1:
        job.start(speakers=speakers)

    else:
        job.start()

@app.command()
def build_file(filepath: str, output_file: Path, format:str='transcript'):
    job = AmazonJob(filepath=filepath, bucket='pit-transcriptions', status='foo')

    if job.status == 'COMPLETED':
        job.build()

        if format == 'transcript':
            output_file.write_text(job.transcript)

        elif  format == 'srt':
            output_file.write_text(job.srt)

    else:
        typer.echo(job.status)


if __name__ == "__main__":
    app()
