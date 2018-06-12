import click
import os


def comp_create(name, path):
    click.echo("Creating component %s ..." % name)
    os.mkdir("{0}/{1}".format(path, name))
    with open("{0}/{1}/{2}.html".format(path, name, name), "w") as html_file:
        html_file.write("")
    with open("{0}/{1}/{2}.css".format(path, name, name), "w") as css_file:
        css_file.write("")
    with open("{0}/{1}/{2}.dart".format(path, name, name), "w") as dart_file:
        dart_file.write("")
    click.echo("Component %s Created" % name)
