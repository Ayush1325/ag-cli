import click
import os


def app_create(app):
    click.echo("Creating app %s ..." % app)
    os.mkdir("%s" % app)
    with open("{0}/{1}.html".format(app, app), "w") as html_file:
        html_file.write("")
    with open("{0}/{1}.css".format(app, app), "w") as css_file:
        css_file.write("")
    with open("{0}/{1}.dart".format(app, app), "w") as dart_file:
        dart_file.write("")
    click.echo("App %s Created" % app)


def comp_create(comp):
    click.echo("Creating component %s ..." % comp)
