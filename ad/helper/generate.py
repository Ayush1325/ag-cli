"""
Function to generate files.
"""

import pystache


def generate(g_path, g_file, s_path, s_file, hash):
    with open("{0}/{1}".format(g_path, g_file), "w") as file, open("{0}/{1}".format(s_path, s_file), "r") as file_skeleton:
        content = pystache.render(file_skeleton.read(), hash)
        file.write(content)
