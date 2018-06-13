import click
import os
import pystache
import pkg_resources


def comp_create(name, path):
    click.echo("Creating component %s ..." % name)
    file = "{0}/{1}/{2}".format(path, name, name)
    os.mkdir("{0}/{1}".format(path, name))
    dart_hash = {
        'selector': 'my-app',
        'stylesheet': '%s.css' % name,
        'html_template': '%s.html' % name,
        'directives': 'CORE_DIRECTIVES',
        'class': 'test'
    }
    abc = "templates/component/component.dart.mustache"
    filepath = pkg_resources.resource_filename(__name__, abc)
    with open("%s.html" % file, "w") as html_file:
        html_file.write("")
    with open("%s.css" % file, "w") as css_file:
        css_file.write("")
    with open("%s.dart" % file, "w") as dart_file, open(filepath, "r") as dart_mustache:
        code = pystache.render(dart_mustache.read(), dart_hash)
        dart_file.write(code)
    click.echo("Component %s Created" % name)
