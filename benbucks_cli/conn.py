import rich_click as click

from .config import CONNECTION_FILE


@click.command(name="conn")
@click.argument("string")
def set_connection_string(string: str):
    """Set your connection string."""
    with CONNECTION_FILE.open("w") as file:
        file.write(string)

    click.secho("Successfully stored connection string", fg="green")
