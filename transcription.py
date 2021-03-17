from pathlib import Path

import typer
from transcriptor.amazon import AmazonEnv

app = typer.Typer()


@app.command()
def upload_file(filepath: str, speakers: int = 1, uploaded: bool = False):
    job = AmazonEnv(audio_file=filepath, bucket="pit-transcriptions")
    job.is_uploaded = uploaded
    job.start_transcription(speaker_count=speakers)


@app.command()
def build_file(filepath: str, output_file: Path):
    job = AmazonEnv(audio_file=filepath, bucket="pit-transcriptions")
    transcription = job.build()
    output_file.write_text(transcription.to_text())


if __name__ == "__main__":
    app()
