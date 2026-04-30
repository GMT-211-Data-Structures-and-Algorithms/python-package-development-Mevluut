import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'PA Package'
copyright = '2026, Student'
author = 'Student'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build']

html_theme = 'furo'
html_static_path = ['_static']
