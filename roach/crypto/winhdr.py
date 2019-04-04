# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

from roach.ints import UInt8, UInt16, UInt32
from roach.structure import Structure

class BLOBHEADER(Structure):
    _pack_ = 1
    _fields_ = [
        ("bType", UInt8),
        ("bVersion", UInt8),
        ("wReserved", UInt16),
        ("aiKeyAlg", UInt32),
    ]

class BaseBlob(object):
    def __init__(self):
        self.bitsize = 0

    def parse(self, buf):
        raise NotImplementedError

    def export_key(self):
        raise NotImplementedError