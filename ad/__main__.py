import click
from .create import app_create
from .create import comp_create


@click.group()
def main():
    pass


@main.command()
@click.option("--app", default=None, help="Create App.")
@click.option("--comp", default=None, help="Create Component.")
def create(app, comp):
    if app:
        app_create(app)
    elif comp:
        comp_create(comp)
    else:
        click.echo(
            """ App or Component parameters needed.\n Refer to --help for more details.""")


if __name__ == '__main__':
    main()
