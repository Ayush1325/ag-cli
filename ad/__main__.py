"""
Angular Dart CLI package.
"""

import click
import inflection
import getpass
import subprocess
from .app_create import app_create
from .component_create import comp_create


@click.group()
def main():
    pass

# Command to generate skeleton angular dart application.


@main.command()
@click.option("--name", "-n", help="Create App.", required=True)
@click.option("--path", "-p", default="", help="Path for creating the app.")
@click.option("--author", "-a", default=getpass.getuser(), help="Author Name.")
@click.option("--pubget", "-pg", is_flag=True, help="Run pub get after generating the project.")
def app(name, path, author, pubget):
    click.echo("Creating name %s ..." % name)
    app_create(name, path, inflection.humanize(author))
    click.echo("App %s Created" % name)
    if pubget:
        subprocess.run('pub get', shell=True)

# Command to generate angular dart component.


@main.command()
@click.option("--name", "-n", help="Create Component.", required=True)
@click.option("--path", "-p",  default="lib/src", help="Path for creating the Component.")
@click.option("--classname", "-c", default="", help="Class Name of Component.(*Optional)")
@click.option("--selector", "-s", default="", help="Selector Name of Component.(*Optional)")
def comp(name, path, classname, selector):
    # if classname:
    #     comp_create(name, path, classname)
    # else:
    #     comp_create(name, path, name)
    click.echo("Creating component %s ..." % name)
    comp_create(inflection.underscore(name), path,
                (lambda c: c if c else inflection.camelize(name))(classname),
                (lambda s: s if s else inflection.dasherize(inflection.underscore(name)))(selector))

    click.echo("Component %s Created" % name)
