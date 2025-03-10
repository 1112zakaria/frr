# -*- coding: utf-8 -*-
#
# FRR documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 31 16:00:52 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import re
import pygments
import sphinx
from sphinx.highlighting import lexers

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.0"

# prolog for various variable substitutions
rst_prolog = ""

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.todo"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"FRR"
copyright = u"2017, FRR"
author = u"FRR authors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = u"?.?"
# The full version, including alpha/beta/rc tags.
release = u"?.?-?"


# -----------------------------------------------------------------------------
# Extract values from codebase for substitution into docs.
# -----------------------------------------------------------------------------

# Various installation prefixes. Values are extracted from config.status.
# Reasonable defaults are set in case that file does not exist.
replace_vars = {
    "AUTHORS": author,
    "COPYRIGHT_YEAR": "1999-2005",
    "COPYRIGHT_STR": "Copyright (c) 1999-2005",
    "PACKAGE_NAME": project.lower(),
    "PACKAGE_TARNAME": project.lower(),
    "PACKAGE_STRING": project.lower() + " latest",
    "PACKAGE_URL": "https://frrouting.org/",
    "PACKAGE_VERSION": "latest",
    "INSTALL_PREFIX_ETC": "/etc/frr",
    "INSTALL_PREFIX_SBIN": "/usr/lib/frr",
    "INSTALL_PREFIX_STATE": "/var/run/frr",
    "INSTALL_PREFIX_MODULES": "/usr/lib/frr/modules",
    "INSTALL_USER": "frr",
    "INSTALL_GROUP": "frr",
    "INSTALL_VTY_GROUP": "frrvty",
    "GROUP": "frr",
    "USER": "frr",
}

# extract version information, installation location, other stuff we need to
# use when building final documents
val = re.compile('^S\["([^"]+)"\]="(.*)"$')
try:
    with open("../../config.status", "r") as cfgstatus:
        for ln in cfgstatus.readlines():
            m = val.match(ln)
            if not m or m.group(1) not in replace_vars.keys():
                continue
            replace_vars[m.group(1)] = m.group(2)
except IOError:
    # if config.status doesn't exist, just ignore it
    pass

# manually fill out some of these we can't get from config.status
replace_vars["COPYRIGHT_STR"] = "Copyright (c)"
replace_vars["COPYRIGHT_STR"] += " {0}".format(replace_vars["COPYRIGHT_YEAR"])
replace_vars["COPYRIGHT_STR"] += " {0}".format(replace_vars["AUTHORS"])
release = replace_vars["PACKAGE_VERSION"]
version = release.split("-")[0]

# add substitutions to prolog
for key, value in replace_vars.items():
    rst_prolog += ".. |{0}| replace:: {1}\n".format(key, value)

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_build",
    "rpki.rst",
    "routeserver.rst",
    "ospf_fundamentals.rst",
    "bgp-linkstate.rst",
    "flowspec.rst",
    "snmptrap.rst",
    "wecmp_linkbw.rst",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "default"

try:
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
except ImportError:
    pass

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#    'sidebarbgcolor': '#374249'
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../figures/frr-icon.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "../figures/frr-logo-icon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "FRRdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "FRR.tex", u"FRR User Manual", u"FRR", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "../figures/frr-logo-medium.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "frr", u"FRR User Manual", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "frr",
        u"FRR User Manual",
        author,
        "FRR",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# contents of ../extra/frrlexer.py.
# This is read here to support VPATH build. Since this section is execfile()'d
# with the file location, we can safely use a relative path here to save the
# contents of the lexer file for later use even if our relative path changes
# due to VPATH.
with open("../extra/frrlexer.py", "rb") as lex:
    frrlexerpy = lex.read()

# Parse version string into int array
def vparse(s):
    a = []

    for c in s:
        if c != ".":
            a.append(int(c))

    while len(a) < 3:
        a.append(0)

    return a[:3]


# custom extensions here
def setup(app):
    # object type for FRR CLI commands, can be extended to document parent CLI
    # node later on
    app.add_object_type("clicmd", "clicmd", indextemplate="pair: %s; configuration command")

    # I dont care how stupid this is
    if "add_js_file" in dir(app):
        app.add_js_file("overrides.js")
    else:
        app.add_javascript("overrides.js")

    if "add_css_file" in dir(app):
        app.add_css_file("overrides.css")
    else:
        app.add_stylesheet("overrides.css")


    # load Pygments lexer for FRR config syntax
    #
    # NB: in Pygments 2.2+ this can be done with `load_lexer_from_file`, but we
    # do it manually since not all of our supported build platforms have 2.2
    # yet.
    #
    # frrlexer = pygments.lexers.load_lexer_from_file('../extra/frrlexer.py', lexername="FRRLexer")
    custom_namespace = {}
    exec(frrlexerpy, custom_namespace)
    lexers["frr"] = custom_namespace["FRRLexer"]()
