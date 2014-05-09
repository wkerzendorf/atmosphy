# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This is an Astropy affiliated package.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

import os
from shutil import copyfile
#import initialize
import logging

atmosphyUserPath = os.path.expanduser('~/.atmosphy')
moduleDir = os.path.dirname(os.path.realpath(__file__))

# Generate the once-off ~/.atmosphy directory

if not os.path.exists(atmosphyUserPath):
    os.makedirs(atmosphyUserPath)
    
#Creating a atmosphy.db3
if not os.path.exists(os.path.join(atmosphyUserPath, 'atmosphy.db3')):
    import sqlite3
    conn = sqlite3.connect(os.path.join(atmosphyUserPath, 'atmosphy.db3'))
    conn.executescript(file(os.path.join(moduleDir, 'conf.d', 'atmosphy.schema')).read())
    conn.commit()
    conn.close()
