import click


@click.group()
def main():
    pass


@main.command()
@click.option("--app", default=None, help="Create App.")
@click.option("--comp", default=None, help="Create Component.")
def create(app, comp):
    if app:
        click.echo("Creating app %s" % app)
    elif comp:
        click.echo("Creating component")
    else:
        click.echo(
            """ App or Component parameters needed.\n Refer to --help for more details.""")


if __name__ == '__main__':
    main()
