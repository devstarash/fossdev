# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
project = 'sales'
copyright = '2026, Nikita Starashchuk'
author = 'Nikita Starashchuk'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc", #Автоматический сбор docsstring
    "sphinx.ext.napoleon", #поддержка стандартов docsstring
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode" #ссылка на код


]
source_suffix = {
    ".md" : "markdown",
    ".rst" : "restructuredtext"
}

autosummary_generate = True



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
