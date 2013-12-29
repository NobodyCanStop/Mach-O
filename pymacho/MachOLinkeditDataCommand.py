# encoding: utf-8

"""
Copyright 2013 Jérémie BOUTOILLE

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from struct import unpack
from pymacho.MachOLoadCommand import MachOLoadCommand
from pymacho.Constants import *


class MachOLinkeditDataCommand(MachOLoadCommand):

    dataoff = 0
    datasize = 0

    def __init__(self, macho_file=None, cmd=0):
        self.cmd = cmd
        if macho_file is not None:
            self.parse(macho_file)

    def parse(self, macho_file):
        self.dataoff, self.datasize = unpack('<II', macho_file.read(4*2))

    def display(self, before=''):
        name = ''
        if self.cmd == LC_CODE_SIGNATURE:
            name = 'LC_CODE_SIGNATURE'
        elif self.cmd == LC_SEGMENT_SPLIT_INFO:
            name = 'LC_SEGMENT_SPLIT_INFO'
        elif self.cmd == LC_FUNCTION_STARTS:
            name = 'LC_FUNCTION_STARTS'
        elif self.cmd == LC_DATA_IN_CODE:
            name = 'LC_DATA_IN_CODE'
        elif self.cmd == LC_DYLIB_CODE_SIGN_DRS:
            name = 'LC_DYLIB_CODE_SIGN_DRS'
        else:
            raise Exception('WHAT DA FUCK')

        print before + "[+] %s" % name
        print before + "\t- dataoff : 0x%x" % self.dataoff
        print before + "\t- datasize : 0x%x" % self.datasize
