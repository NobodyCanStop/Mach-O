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

# MAGIC
MH_MAGIC = 0xfeedface
MH_CIGAM = 0xcefaedfe
MH_MAGIC_64 = 0xfeedfacf
MH_CIGAM_64 = 0xcffaedfe

# CPUTYPE
CPU_TYPE_POWERPC = 0x12
CPU_TYPE_POWERPC64 = 0x1000012
CPU_TYPE_I386 = 0x7
CPU_TYPE_X86_64 = 0x1000007
CPU_TYPE_MC680x0 = 0x6
CPU_TYPE_HPPA = 0xb
CPU_TYPE_I860 = 0xf
CPU_TYPE_MC88000 = 0xd
CPU_TYPE_SPARC = 0xe

# FILETYPE
MH_OBJECT = 0x1         # relocatable object file
MH_EXECUTE = 0x2        # demand paged executable file
MH_FVMLIB = 0x3         # fixed VM shared library file
MH_CORE = 0x4           # core file
MH_PRELOAD = 0x5        # preloaded executable file
MH_DYLIB = 0x6          # dynamically bound shared library
MH_DYLINKER = 0x7       # dynamic link editor
MH_BUNDLE = 0x8         # dynamically bound bundle file
MH_DYLIB_STUB = 0x9     # shared library stub for static linking only, no section contents
MH_DSYM = 0xa           # companion file with only debug sections
MH_KEXT_BUNDLE = 0xb    # x86_64 kexts

# FLAGS MASK
MH_NOUNDEFS = 0x1
MH_INCRLINK = 0x2
MH_DYLDLINK = 0x4
MH_BINDATLOAD = 0x8
MH_PREBOUND = 0x10
MH_SPLIT_SEGS = 0x20
MH_LAZY_INIT = 0x40
MH_TWOLEVEL = 0x80
MH_FORCE_FLAT = 0x100
MH_NOMULTIDEFS = 0x200
MH_NOFIXPREBINDING = 0x400
MH_PREBINDABLE = 0x800
MH_ALLMODSBOUND = 0x1000
MH_SUBSECTIONS_VIA_SYMBOLS = 0x2000
MH_CANONICAL = 0x4000
MH_WEAK_DEFINES = 0x8000
MH_BINDS_TO_WEAK = 0x10000
MH_ALLOW_STACK_EXECUTION = 0x20000
MH_ROOT_SAFE = 0x40000
MH_SETUID_SAFE = 0x80000
MH_SETUID_SAFE = 0x80000
MH_NO_REEXPORTED_DYLIBS = 0x100000
MH_PIE = 0x200000
MH_DEAD_STRIPPABLE_DYLIB = 0x400000
MH_HAS_TLV_DESCRIPTORS = 0x800000
MH_NO_HEAP_EXECUTION = 0x1000000

# LOAD COMMANDS
LC_REQ_DYLD = 0x80000000
LC_SEGMENT = 0x1
LC_SYMTAB = 0x2
LC_SYMSEG = 0x3
LC_THREAD = 0x4
LC_UNIXTHREAD = 0x5
LC_LOADFVMLIB = 0x6
LC_IDFVMLIB = 0x7
LC_IDENT = 0x8
LC_FVMFILE = 0x9
LC_PREPAGE = 0xa
LC_DYSYMTAB = 0xb
LC_LOAD_DYLIB = 0xc
LC_ID_DYLIB = 0xd
LC_LOAD_DYLINKER = 0xe
LC_ID_DYLINKER = 0xf
LC_PREBOUND_DYLIB = 0x10
LC_ROUTINES = 0x11
LC_SUB_FRAMEWORK = 0x12
LC_SUB_UMBRELLA = 0x13
LC_SUB_CLIENT = 0x14
LC_SUB_LIBRARY = 0x15
LC_TWOLEVEL_HINTS = 0x16
LC_PREBIND_CKSUM = 0x17
LC_LOAD_WEAK_DYLIB = (0x18 | LC_REQ_DYLD)
LC_SEGMENT_64 = 0x19
LC_ROUTINES_64 = 0x1a
LC_UUID = 0x1b
LC_RPATH = (0x1c | LC_REQ_DYLD)
LC_CODE_SIGNATURE = 0x1d
LC_SEGMENT_SPLIT_INFO = 0x1e
LC_REEXPORT_DYLIB = (0x1f | LC_REQ_DYLD)
LC_LAZY_LOAD_DYLIB = 0x20
LC_ENCRYPTION_INFO = 0x21
LC_DYLD_INFO = 0x22
LC_DYLD_INFO_ONLY = (0x22 | LC_REQ_DYLD)
LC_LOAD_UPWARD_DYLIB = (0x23 | LC_REQ_DYLD)
LC_VERSION_MIN_MACOSX = 0x24
LC_VERSION_MIN_IPHONEOS = 0x25
LC_FUNCTION_STARTS = 0x26
LC_DYLD_ENVIRONMENT = 0x27