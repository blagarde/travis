#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import unicodecsv
from unicodecsv import DictReader
import sys
print(sys.version)
try:
    import StringIO as io
except ImportError:
    pass  # Python >= 3
from io import StringIO
d = DictReader(StringIO('a,b,c\n1,2,3'))
print('yay')
