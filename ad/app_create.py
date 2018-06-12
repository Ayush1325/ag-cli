import click
import os


def app_create(name):
    click.echo("Creating name %s ..." % name)
    click.echo("App %s Created" % name)
