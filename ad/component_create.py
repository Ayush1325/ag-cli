import os
import pkg_resources
from .helper.generate import generate


def comp_create(name, path, class_name, selector):
    file = "{0}_component".format(name)
    os.mkdir("{0}/{1}".format(path, name))
    skeleton_files = "templates/component"
    filepath = pkg_resources.resource_filename(__name__, skeleton_files)
    files = ["%s.html" % file, "%s.css" % file, "%s.dart" % file]
    hash = {
        "%s.html" % file: {},
        "%s.css" % file: {},
        "%s.dart" % file: {
            'selector': selector,
            'stylesheet': name,
            'html_template': name,
            'directives': 'CORE_DIRECTIVES',
            'class': class_name
        }
    }
    skeleton = {
        "%s.html" % file: "component.html.mustache",
        "%s.css" % file: "component.css.mustache",
        "%s.dart" % file: "component.dart.mustache"
    }
    for file in files:
        generate("{0}/{1}".format(path, name), file,
                 filepath, skeleton[file], hash[file])
