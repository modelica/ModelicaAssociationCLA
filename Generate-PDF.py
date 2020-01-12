#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (C) 2020, Modelica Association and contributors
All rights reserved.

Generate ModelicaAssociationCLA_1.1.1.pdf
python Generate-PDF.py
'''

import requests
import os
import os.path
import sys

def main(dir, version):
    template = 'ModelicaAsscociationCLA-Template.html'
    file_name = 'ModelicaAssociationCLA.md'
    file_name_pdf = 'ModelicaAssociationCLA_{0}.pdf'.format(version)

    # Convert Markdown -> PDF
    with open(os.path.join(dir, file_name_pdf), 'wb') as f:
        url = 'http://c.docverter.com/convert'
        css = 'docverter.css'
        with open(css, 'w') as c:
            pageInfo = 'body {font-size: 10pt;} @page {size: A4 portrait; margin: 1in; @bottom-center{font-size: 10pt; content: counter(page)}}'
            c.write(pageInfo)
        data = {'to': 'pdf', 'from': 'markdown', 'css': css, 'template': template}
        files = [ \
            ('input_files[]', (file_name, open(os.path.join(dir, file_name), 'rb'), 'text/markdown')), \
            ('other_files[]', (template, open(os.path.join(dir, template), 'rb'), 'text/html')), \
            ('other_files[]', (css, open(os.path.join(dir, css), 'rb'), 'text/css')) \
        ]
        r = requests.post(url, data=data, files=files)
        f.write(r.content)

if __name__ == '__main__':
    module_dir, _ = os.path.split(__file__)
    version = '1.1.1'

    main(module_dir, version)
