from routes import mysite
import typer

def build(
        verbose: bool = typer.Option(False, '--verbose', '-n'),
        clean: bool = typer.Option(False, '--clean'),
        update: bool = typer.Option(False, '--update', '-U'),
        ):

    if clean or update:
        return mysite.render(strict=True, verbose=verbose)

    return mysite.render(verbose=verbose)


if __name__ == "__main__":
    typer.run(build)

