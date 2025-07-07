"""Custom CLI for scipyconference.

This is totally optional;
if you want to use it, though,
follow the skeleton to flesh out the CLI to your liking!
Finally, familiarize yourself with Typer,
which is the package that we use to enable this magic.
Typer's docs can be found at:

    https://typer.tiangolo.com
"""

import typer

from .bots import punbot

app = typer.Typer()


@app.command()
def create_puns(number: int):
    """Create `number` of puns for the SciPy conference."""

    for i in range(number):
        punbot()


@app.command()
def describe():
    """Describe the project."""
    typer.echo("Making the T-shirt puns work!")


if __name__ == "__main__":
    app()
