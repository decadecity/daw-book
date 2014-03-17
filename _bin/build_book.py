#!/usr/bin/python
import os
import sys

BASE_PATH = os.path.normpath(os.path.dirname(__file__))
sys.path.append(BASE_PATH + '/../_lib/markdown')

import markdown

from pprint import pprint

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.


    # Walk the tree.
    for root, directories, files in os.walk(directory):
        root = os.path.normpath(root)
        directories.sort()
        #pprint(directory)
        files.sort()
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if not root.startswith('_') and filename.endswith(".md"):
                filepath = os.path.normpath(os.path.join(root, filename))
                file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths(BASE_PATH + '/..')

#pprint(full_file_paths)

book = '';

last_dirname = ''
for path in full_file_paths:
    if '/' in path:
        dirname, filename = path.split('/')
        if dirname != last_dirname:
            book += '\n<hr/>\n<p><code class="filename">' + path + '</code></p>\n'
        with open(path) as f:
            book += markdown.markdown(f.read(), output_format='HTML5')

template = """<!DOCTYPE html>
<html>
  <head>
    <title>Building for the Device Agnostic Web</title>
    <link rel="stylesheet" href="book.css">
  </head>
  <body>
%s
  </body>
</html>
"""

print(template % book)

