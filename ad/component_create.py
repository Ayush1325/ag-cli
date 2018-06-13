import click
import os


def comp_create(name, path):
    click.echo("Creating component %s ..." % name)
    file = "{0}/{1}/{2}".format(path, name, name)
    os.mkdir("{0}/{1}".format(path, name))
    with open("%s.html" % file, "w") as html_file:
        html_file.write("")
    with open("%s.css" % file, "w") as css_file:
        css_file.write("")
    with open("%s.dart" % file, "w") as dart_file:
        dart_file.write("")
    click.echo("Component %s Created" % name)
