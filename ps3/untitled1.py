# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 14:44:56 2018

@author: Ike
"""

import uncompyle6
with open("test.py", "w") as fileobj:
    uncompyle6.uncompyle_file("test.pyc", fileobj)
    
fileobj.close()