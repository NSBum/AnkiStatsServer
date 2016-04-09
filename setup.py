#!/usr/bin/python

import os, subprocess, sys
#subprocess.call(['python', 'virtualenv.py', 'flask'])
if sys.platform == 'win32':
    bin = 'Scripts'
else:
    bin = 'bin'
    try:
        subprocess.call(['pip', 'install', 'mysql-python'])
        subprocess.call(['pip', 'install', 'flask'])
        subprocess.call(['pip', 'install', 'flask-login'])
        subprocess.call(['pip', 'install', 'sqlalchemy'])
        subprocess.call(['pip', 'install', 'flask-sqlalchemy'])
        subprocess.call(['pip', 'install', 'sqlalchemy-migrate'])
    except OSError as e:
        print "OS Error {0}: {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
