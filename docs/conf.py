import sys
import os
import shlex
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
ource_suffix = '.rst'
master_doc = 'index'
project = u'Accounts Monster'
copyright = u'2015, Adam Terrey'
author = u'Adam Terrey'
version = '0.01'
release = '0.01'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'AccountsMonsterdoc'
latex_elements = {}
latex_documents = [
  (master_doc, 'AccountsMonster.tex', u'Accounts Monster Documentation',
   u'Accounts Monster', 'manual'),
]
man_pages = [
    (master_doc, 'accountsmonster', u'Accounts Monster Documentation',
     [author], 1)
]
texinfo_documents = [
  (master_doc, 'AccountsMonster', u'Accounts Monster Documentation',
   author, 'AccountsMonster', 'One line description of project.',
   'Miscellaneous'),
]
