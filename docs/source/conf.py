# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'FigureStream'
copyright = '2021, Yeison Cardona'
author = 'Yeison Cardona'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',

    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',

    'nbsphinx',
    'sphinx.ext.mathjax',
]

naoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_theme_options = {
    'page_width': '1280px',
    'sidebar_width': '300px',
}

html_static_path = ['_static']

html_sidebars = {
    '**': [
        # 'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'FigureStreamdoc'


# -- Extension configuration -------------------------------------------------

autodoc_mock_imports = [

    'browser',

    'IPython',
    'numpy',
    'scipy',
    'mne',
    'matplotlib',
    'google',
    'colorama',
    'tqdm',
    'pandas',
    'tables',
    'pyedflib',
    'netifaces',
    'nmap',
    'rawutil',
    'kafka',
    'rpyc',
    'serial',


]


todo_include_todos = True


html_logo = '_static/logo.svg'
html_favicon = '_static/favico.ico'

# autodoc_default_options = [
    # 'members',
    # 'no-undoc-members',
    # 'show-inheritance',
# ]

# autodoc_default_options = {
    # 'members': 'var1, var2',
    # 'member-order': 'bysource',
    # 'special-members': '__init__',
    # 'undoc-members': True,
    # 'exclude-members': '__weakref__'
# }


def setup(app):
    app.add_css_file("custom.css")


highlight_language = 'none'
html_sourcelink_suffix = ''

# nbsphinx_execute_arguments = [
    # "--InlineBackend.figure_formats={'svg', 'pdf'}",
    # "--InlineBackend.rc={'figure.dpi': 96}",
# ]

nbsphinx_execute = 'never'
# nbsphinx_input_prompt = ' '
# nbsphinx_output_prompt = ' '
nbsphinx_kernel_name = 'python3'
nbsphinx_prompt_width = '0'


nbsphinx_prolog = """
.. raw:: html

    <style>
        .nbinput .prompt,
        .nboutput .prompt {
            display: none;
    }
    </style>
"""


def get_notebooks(notebooks_dir, exclude=[]):
    notebooks_list = os.listdir(os.path.join(
        os.path.abspath(os.path.dirname(__file__)), notebooks_dir))
    notebooks_list = filter(lambda s: not s.startswith('__'), notebooks_list)

    notebooks = []
    for notebook in notebooks_list:
        if notebook not in exclude and notebook.endswith('.ipynb'):
            notebooks.append(f"{notebooks_dir}/{notebook.replace('.ipynb', '')}")

    notebooks = '\n   '.join(sorted(notebooks))
    return notebooks


notebooks = get_notebooks('notebooks', exclude=['readme.ipynb', 'license.ipynb'])


with open('index.rst', 'w') as file:
    file.write(f"""

.. include:: notebooks/readme.rst


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

    """)

