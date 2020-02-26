import os

from pykv.interface import PyKV

__version__ = "1.0"
__all__ = ['PyKV', 'connect']


def connect(dbname):
    try:
        f = open(dbname, 'r+b')
    except IOError:
        fd = os.open(dbname, os.O_RDWR | os.O_CREAT)
        f = os.fdopen(fd, 'r+b')
    return PyKV(f)
