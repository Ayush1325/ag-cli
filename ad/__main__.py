import click
from .app_create import app_create
from .component_create import comp_create


@click.group()
def main():
    pass


@main.command()
@click.option("--name", help="Create App.", required=True)
@click.option("--path", default="", help="Path for creating the app.")
def app(name, path):
    app_create(name, path)


@main.command()
@click.option("--name", help="Create Component.", required=True)
@click.option("--path", default="lib/src", help="Path for creating the Component.")
def comp(name, path):
    comp_create(name, path)


if __name__ == '__main__':
    main()
