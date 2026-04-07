# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Add project root so Sphinx can find modules

# -- Project information -----------------------------------------------------

project = 'Task Manager'
copyright = '2026, Cameron H'
author = 'Cameron H'
release = '0.1'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',      # Auto-generate documentation from docstrings
    'sphinx.ext.napoleon',     # Support Google and NumPy style docstring
]

# Show type hints in the description rather than the signature
autodoc_typehints = 'description'

# Paths for templates and static files
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Language
language = 'eng'

# -- Options for HTML output -------------------------------------------------

# HTML theme
html_theme = 'sphinx_rtd_theme'  # ReadTheDocs style
html_static_path = ['_static']

# -- Optional settings -------------------------------------------------------

# Include both class and __init__ docstrings
autoclass_content = 'both'
