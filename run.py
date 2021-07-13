import typer
import podreader

from routes import mysite


def build(
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    clean: bool = typer.Option(False, "--clean"),
    update: bool = typer.Option(False, "--update", "-u"),
):


    if clean or update:
        return mysite.render(strict=True, verbose=verbose)

    return mysite.render(verbose=verbose)


if __name__ == "__main__":
    typer.run(build)
