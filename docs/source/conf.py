# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx_rtd_theme  # [중요] 테마 모듈 임포트

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sentinema'
copyright = '2025, Jang Jiwon, Lee Mingi'
author = 'Jang Jiwon, Lee Mingi'

# The full version, including alpha/beta/rc tags
# README와 Release Note에 적은 버전과 통일합니다.
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 여기에 필요한 확장 기능들을 추가해야 문서가 예쁘게 나옵니다.
extensions = [
    'sphinx_rtd_theme',       # 테마 적용용
    'sphinx.ext.autodoc',     # (선택사항) 나중에 코드 자동 문서화할 때 필요
    'sphinx.ext.viewcode',    # (선택사항) 소스 코드 링크 생성
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# 테마 설정 (반드시 sphinx_rtd_theme 모듈을 사용하도록 설정)
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
