# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import, print_function, unicode_literals

from mozbuild.util import EnumString
from collections import OrderedDict


CompilerType = EnumString.subclass(
    'clang',
    'clang-cl',
    'gcc',
    'msvc',
)

OS = EnumString.subclass(
    'Android',
    'DragonFly',
    'FreeBSD',
    'GNU',
    'iOS',
    'NetBSD',
    'OpenBSD',
    'OSX',
    'WINNT',
)

Kernel = EnumString.subclass(
    'Darwin',
    'DragonFly',
    'FreeBSD',
    'kFreeBSD',
    'Linux',
    'NetBSD',
    'OpenBSD',
    'WINNT',
)

CPU = EnumString.subclass(
    'aarch64',
    'Alpha',
    'arm',
    'hppa',
    'ia64',
    'mips32',
    'mips64',
    'ppc',
    'ppc64',
    's390',
    's390x',
    'sparc',
    'sparc64',
    'x86',
    'x86_64',
)

Endianness = EnumString.subclass(
    'big',
    'little',
)

# The order of those checks matter
CPU_preprocessor_checks = OrderedDict((
    ('x86', '__i386__ || _M_IX86'),
    ('x86_64', '__x86_64__ || _M_X64'),
    ('arm', '__arm__ || _M_ARM'),
    ('aarch64', '__aarch64__'),
    ('ia64', '__ia64__'),
    ('s390x', '__s390x__'),
    ('s390', '__s390__'),
    ('ppc64', '__powerpc64__'),
    ('ppc', '__powerpc__'),
    ('Alpha', '__alpha__'),
    ('hppa', '__hppa__'),
    ('sparc64', '__sparc__ && __arch64__'),
    ('sparc', '__sparc__'),
    ('mips64', '__mips64'),
    ('mips32', '__mips__'),
))

assert sorted(CPU_preprocessor_checks.keys()) == sorted(CPU.POSSIBLE_VALUES)

kernel_preprocessor_checks = {
    'Darwin': '__APPLE__',
    'DragonFly': '__DragonFly__',
    'FreeBSD': '__FreeBSD__',
    'kFreeBSD': '__FreeBSD_kernel__',
    'Linux': '__linux__',
    'NetBSD': '__NetBSD__',
    'OpenBSD': '__OpenBSD__',
    'WINNT': '_WIN32 || __CYGWIN__',
}

assert sorted(kernel_preprocessor_checks.keys()) == sorted(Kernel.POSSIBLE_VALUES)
