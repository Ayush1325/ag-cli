import click
import os


def comp_create(name):
    click.echo("Creating component %s ..." % name)
    os.mkdir("%s" % name)
    with open("{0}/{1}.html".format(name, name), "w") as html_file:
        html_file.write("")
    with open("{0}/{1}.css".format(name, name), "w") as css_file:
        css_file.write("")
    with open("{0}/{1}.dart".format(name, name), "w") as dart_file:
        dart_file.write("")
    click.echo("Component %s Created" % name)
