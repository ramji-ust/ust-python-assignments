import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    A simple command that greets the user.
    """
    typer.echo(f"Hello {name}!")