import os
import pystache
import pkg_resources
import shutil


def app_create(name, path, author):
    path = "{0}{1}".format(path, name)
    os.mkdir(path)
    os.mkdir("%s/lib" % path)
    os.mkdir("%s/test" % path)
    os.mkdir("%s/web" % path)
    os.mkdir("%s/lib/src" % path)
    skeleton_files = "templates/app"
    filepath = pkg_resources.resource_filename(__name__, skeleton_files)

    with open("%s/README.md" % path, "w") as readme, open("%s/README.md.mustache" % filepath, "r") as readme_skeleton:
        content = pystache.render(readme_skeleton.read(), {
                                  'projectName': name})
        readme.write(content)

    with open("%s/pubspec.yaml" % path, "w") as pubspec, open("%s/pubspec.yaml.mustache" % filepath, "r") as pubspec_skeleton:
        content = pystache.render(pubspec_skeleton.read(), {
                                  'projectName': name,
                                  'author': author})
        pubspec.write(content)

    with open("%s/CHANGELOG.md" % path, "w") as changelog, open("%s/CHANGELOG.md.mustache" % filepath, "r") as changelog_skeleton:
        changelog.write(changelog_skeleton.read())

    with open("%s/analysis_options.yaml" % path, "w") as analysis, open("%s/analysis_options.yaml.mustache" % filepath, "r") as analysis_skeleton:
        analysis.write(analysis_skeleton.read())

    with open("%s/.gitignore" % path, "w") as gitignore, open("%s/.gitignore.mustache" % filepath, "r") as gitignore_skeleton:
        gitignore.write(gitignore_skeleton.read())

    with open("%s/web/index.html" % path, "w") as index, open("%s/web_skeleton/index.html.mustache" % filepath, "r") as index_skeleton:
        content = pystache.render(index_skeleton.read(), {
                                  'projectName': name})
        index.write(content)

    with open("%s/web/main.dart" % path, "w") as main, open("%s/web_skeleton/main.dart.mustache" % filepath, "r") as main_skeleton:
        content = pystache.render(main_skeleton.read(), {
                                  'projectName': name})
        main.write(content)

    with open("%s/web/styles.css" % path, "w") as css, open("%s/web_skeleton/styles.css.mustache" % filepath, "r") as css_skeleton:
        css.write(css_skeleton.read())

    shutil.copy("% s/web_skeleton/favicon.png" % filepath, "%s/web" % path)

    with open("%s/test/app_test.dart" % path, "w") as test, open("%s/test_skeleton/app_test.dart.mustache" % filepath, "r") as test_skeleton:
        content = pystache.render(test_skeleton.read(), {'projectName': name})
        test.write(content)

    with open("%s/lib/app_component.css" % path, "w") as component_css, open("%s/lib_skeleton/app_component.css.mustache" % filepath, "r") as component_css_skeleton:
        component_css.write(component_css_skeleton.read())

    with open("%s/lib/app_component.dart" % path, "w") as component_dart, open("%s/lib_skeleton/app_component.dart.mustache" % filepath, "r") as component_dart_skeleton:
        component_dart.write(component_dart_skeleton.read())

    with open("%s/lib/app_component.html" % path, "w") as component_html, open("%s/lib_skeleton/app_component.html.mustache" % filepath, "r") as component_html_skeleton:
        component_html.write(component_html_skeleton.read())
