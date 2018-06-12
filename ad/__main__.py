import click
from .app_create import app_create
from .component_create import comp_create


@click.group()
def main():
    pass


@main.command()
@click.option("--name", help="Create App.")
@click.option("--path", default="")
def app(name, path):
    app_create(name)


@main.command()
@click.option("--name", help="Create Component.")
@click.option("--path", default="lib/src")
def comp(name, path):
    comp_create(name)


if __name__ == '__main__':
    main()
