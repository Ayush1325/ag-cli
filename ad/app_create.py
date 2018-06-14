"""
Function to create Angular Dart app.
"""

import os
import pkg_resources
import shutil
import inflection
from .helper.generate import generate


def app_create(name, path, author):
    path = "{0}{1}".format(path, name)

    # Create app directory.
    os.mkdir(path)

    name = inflection.underscore(name)
    # Create other directories inside the app.
    os.mkdir("%s/lib" % path)
    os.mkdir("%s/test" % path)
    os.mkdir("%s/web" % path)
    os.mkdir("%s/lib/src" % path)

    # Skeleton files path.
    skeleton_files = "templates/app"
    filepath = pkg_resources.resource_filename(__name__, skeleton_files)

    # List of files to be created in the base app folder.
    base_files = ["README.md", "pubspec.yaml",
                  "CHANGELOG.md", "analysis_options.yaml", ".gitignore"]
    # Hashes of base files.
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

    # Deleting variables which are no longer required.
    del base_files, base_hash

    # List of files to be created in the base app/web folder.
    web_files = ["index.html", "main.dart", "styles.css"]
    # Hashes of app/web files.
    web_hash = {
        "index.html": {'projectName': name},
        "main.dart": {'projectName': name},
        "styles.css": {}
    }

    for file in web_files:
        generate("{0}/{1}".format(path, "web"), file, "{0}/{1}".format(filepath, "web_skeleton"),
                 "%s.mustache" % file, web_hash[file])

    # Deleting variables which are no longer required.
    del web_files, web_hash

    # Copying favicon.png to app/web folder.
    shutil.copy("% s/web_skeleton/favicon.png" % filepath, "%s/web" % path)

    generate("{0}/{1}".format(path, "test"), "app_test.dart", "{0}/{1}".format(filepath, "test_skeleton"),
             "app_test.dart.mustache", {'projectName': name})

    # List of files to be created in the base app/lib folder.
    lib_files = ["app_component.css",
                 "app_component.dart", "app_component.html"]

    for file in lib_files:
        generate("{0}/{1}".format(path, "lib"), file, "{0}/{1}".format(filepath, "lib_skeleton"),
                 "%s.mustache" % file, {})

    # Deleting variables which are no longer required.
    del lib_files

    # Changing python working directory to app directory.
    os.chdir(path)
