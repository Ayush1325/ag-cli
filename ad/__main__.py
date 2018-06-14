"""
Angular Dart CLI package.
"""

import click
import inflection
import getpass
import subprocess
from .app_create import app_create
from .component_create import comp_create

# Alternate -h parameter for --help.
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass

# Command to generate skeleton angular dart application.


@main.command()
@click.option("--name", "-n", help="Create App.", required=True)
@click.option("--path", "-p", default="", help="Path for creating the app.(*Optional)")
@click.option("--author", "-a", default=getpass.getuser(), help="Author Name.(*Optional)")
@click.option("--pubget", "-pg", is_flag=True, help="Run pub get after generating the project.(*Optional)")
def app(name, path, author, pubget):
    """To Create App."""
    click.echo("Creating name %s ..." % name)
    app_create(name, path, inflection.humanize(author))
    click.echo("App %s Created" % name)
    if pubget:
        subprocess.run('pub get', shell=True)

# Command to generate angular dart component.


@main.command("comp")
@click.option("--name", "-n", help="Create Component.", required=True)
@click.option("--path", "-p",  default="lib/src", help="Path for creating the Component.(*Optional)")
@click.option("--classname", "-c", default="", help="Class Name of Component.(*Optional)")
@click.option("--selector", "-s", default="", help="Selector Name of Component.(*Optional)")
def component(name, path, classname, selector):
    """To Create Component."""
    click.echo("Creating component %s ..." % name)
    comp_create(inflection.underscore(name), path,
                (lambda c: c if c else inflection.camelize(name))(classname),
                (lambda s: s if s else inflection.dasherize(inflection.underscore(name)))(selector))

    click.echo("Component %s Created" % name)


@main.command()
def serve():
    """To Serve The App."""
    subprocess.run('webdev serve', shell=True)


@main.command()
def build():
    """To Build The App."""
    subprocess.run('webdev build', shell=True)
