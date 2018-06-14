import os
import pkg_resources
import shutil
from .helper.generate import generate


def app_create(name, path, author):
    path = "{0}{1}".format(path, name)
    os.mkdir(path)
    os.mkdir("%s/lib" % path)
    os.mkdir("%s/test" % path)
    os.mkdir("%s/web" % path)
    os.mkdir("%s/lib/src" % path)
    skeleton_files = "templates/app"
    filepath = pkg_resources.resource_filename(__name__, skeleton_files)

    base_files = ["README.md", "pubspec.yaml",
                  "CHANGELOG.md", "analysis_options.yaml", ".gitignore"]
    base_hash = {
        "README.md": {'projectName': name},
        "pubspec.yaml": {'projectName': name, 'author': author},
        "CHANGELOG.md": {},
        "analysis_options.yaml": {},
        ".gitignore": {}
    }
    for file in base_files:
        generate(path, file, filepath,
                 "%s.mustache" % file, base_hash[file])
    del base_files, base_hash

    web_files = ["index.html", "main.dart", "styles.css"]
    web_hash = {
        "index.html": {'projectName': name},
        "main.dart": {'projectName': name},
        "styles.css": {}
    }
    for file in web_files:
        generate("{0}/{1}".format(path, "web"), file, "{0}/{1}".format(filepath, "web_skeleton"),
                 "%s.mustache" % file, web_hash[file])
    del web_files, web_hash

    shutil.copy("% s/web_skeleton/favicon.png" % filepath, "%s/web" % path)

    generate("{0}/{1}".format(path, "test"), "app_test.dart", "{0}/{1}".format(filepath, "test_skeleton"),
             "app_test.dart.mustache", {'projectName': name})

    lib_files = ["app_component.css",
                 "app_component.dart", "app_component.html"]
    for file in lib_files:
        generate("{0}/{1}".format(path, "lib"), file, "{0}/{1}".format(filepath, "lib_skeleton"),
                 "%s.mustache" % file, {})
    del lib_files

    os.chdir(path)
