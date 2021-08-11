#!/usr/bin/env python3
"""The script provides a GUI interface for converting bibtex to the markdown style which is used in this repo.
The user may need to install these external packages:

Usage:
    pip install bibtexparser PyQt5
    ./ref_convert.py

Author:
    weipeng0098@126.com - 2021/8/10 17:16

Version:
    0.0.1

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit, QFormLayout, QApplication
from bibtexparser.bparser import BibTexParser
import bibtexparser
import re


def handle_title(_title: str):
    _title = re.compile('[{}]').sub('', _title.strip())
    return _title


def handle_author(author: str):
    author = ', '.join(list(map(lambda x: ' '.join(x.strip().split(', ')[::-1]), author.split('and'))))
    return author


def handle_url(url: str):
    try:
        arxiv_identifier = re.compile('http://arxiv.org/abs/([\d\.]+)').findall(url)[0]
        url = f'http://arxiv.org/pdf/{arxiv_identifier}.pdf'
    except:
        pass
    return url


def bib_parser(bibref: str):
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False
    bib = bibtexparser.loads(bibref, parser)

    lines = []

    for entry in bib.entries:
        title = handle_title(entry['title'])
        author = handle_author(entry['author'])
        try:
            journal = entry['journal']
        except:
            journal = '**UNKNOWN_JOURNAL**'

        try:
            year = entry['year']
        except:
            year = '**UNKNOWN_YEAR**'
        try:
            url = entry['url']
            url = handle_url(url)
        except:
            url = ''
        lines.append(f"1. **{title}**, *{author}*, {journal}, {year}. [[paper]({url})][[code]()]")
    target = '\n'.join(lines)
    return target


def bib_convert():
    bibtex_str = bib_parser(bibtexEdit.toPlainText())
    targetEdit.setPlainText(bibtex_str)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Bibtex-Markdown converter')
layout = QFormLayout()

bibtexEdit = QPlainTextEdit()
layout.addRow('bibtex:', bibtexEdit)
bibtexEdit.setFixedWidth(1000)

targetEdit = QPlainTextEdit()
layout.addRow('markdown:', targetEdit)
targetEdit.setFixedWidth(1000)

btn = QPushButton('Convert')
btn.clicked.connect(bib_convert)
layout.addRow('Convert', btn)

btn = QPushButton('Clear')
btn.clicked.connect(bibtexEdit.clear)
btn.clicked.connect(targetEdit.clear)
layout.addRow('Clear', btn)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
