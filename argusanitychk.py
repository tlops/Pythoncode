#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
def sanitychk ():
    if len(sys.argv)<3:
        print ('{} : Requires two argument'.format(sys.argv[0]))
        print ('Usage: {} filename word'.format(sys.argv[0]))
        return (1)
        sys.exit()

        filename = sys.argv[1]
        text  = sys.argv[2]


