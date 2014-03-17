#!/usr/bin/env python
#
# A quick script to adjust latex output
#!TODO: This would be better done with the nbconvert machinary

import sys
import re
import os
from urllib2 import urlopen

fn = sys.argv[1]

new_lines = []
fh = open(fn)
for line in fh:
    line = re.sub(r'\\documentclass\[letterpaper', r'\\documentclass[a4paper', line)
    line = re.sub(r'\\includegraphics\[max size=\{\\textwidth\}', 
                  r'\\includegraphics[max size={0.6\\textwidth}', line)

    #line = re.sub(r'\\def\\smaller\{\\fontsize\{9.5pt\}\{9.5pt\}', 
    #              r'\\def\\smaller{\\fontsize{8.5pt}{8.5pt}', line) 
    line = re.sub(r'\\begin\{alltt\}', r'\\footnotesize\\begin{alltt}', line)
    line = re.sub(r'\\end\{alltt\}', r'\\end{alltt}\\normalsize', line)

    # Detect included http references
    mo = re.search(r'\\includegraphics\{(http.*?)\}', line)
    if mo:
        url = mo.group(1)
        filename = url.split('/')[-1]
        if not os.path.exists(filename):
            url_h = urlopen(url)
            data = url_h.read()
            open(filename, 'w').write(data)
        
        line = re.sub(r'\\includegraphics\{http.*?\}', 
                      r'\\includegraphics[max size={0.6\\textwidth}{\\textheight}]{%s}' % filename, line)
        
    new_lines.append(line)

fh.close()

fh = open(fn, 'w')
for line in new_lines:
    fh.write(line)
