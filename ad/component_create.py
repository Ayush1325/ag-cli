import click
import os
import pystache
import pkg_resources
import inflection


def comp_create(name, path, class_name):
    click.echo("Creating component %s ..." % name)
    name = inflection.underscore(name)
    class_name = inflection.camelize(class_name)
    file = "{0}/{1}/{2}_component".format(path, name, name)
    os.mkdir("{0}/{1}".format(path, name))
    dart_hash = {
        'selector': 'my-app',
        'stylesheet': '{0}_component'.format(name),
        'html_template': '{0}_component'.format(name),
        'directives': 'CORE_DIRECTIVES',
        'class': class_name
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
