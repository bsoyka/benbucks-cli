import rich_click as click

from .conn import set_connection_string


@click.group()
def main():
    pass


main.add_command(set_connection_string)
