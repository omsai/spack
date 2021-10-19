# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Htop(AutotoolsPackage):
    """htop is an interactive text-mode process viewer for Unix systems."""

    homepage = "https://htop.dev"
    url      = "https://github.com/htop-dev/htop/archive/refs/tags/3.1.1.tar.gz"

    maintainers = ['omsai']

    version('3.1.1', sha256='b52280ad05a535ec632fbcd47e8e2c40a9376a9ddbd7caa00b38b9d6bb87ced6')

    variant('sensors', default=True, description='Support reading temperature data')
    variant('affinity', default='hwloc', description='Support CPU affinity',
            values=('hwloc', 'capabilities', 'none'), multi=False)
    variant('delayacct', default=True, description='Linux delay accounting support')
    variant('virt', default='none', description='Support virtualization',
            values=('openvz', 'vserver', 'ancient-vserver', 'none'), multi=True)

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('pkgconf', type='build')

    depends_on('ncurses@6:')
    depends_on('python+pythoncmd', type='build')

    depends_on('lm-sensors', when='+sensors')
    depends_on('hwloc', when='affinity=hwloc')
    depends_on('libcap', when='affinity=capabilities')
    depends_on('libnl', when='+delayacct')

    def configure_args(self):
        args = []

        # Dependency related flags.
        for flag in 'sensors delayacct'.split():
            if '+' + flag in self.spec:
                args.append('--enable-' + flag)
            else:
                args.append('--disable-' + flag)

        if 'none' in self.spec.variants['affinity']:
            args.append('--disable-hwloc')
            args.append('--disable-capabilities')
        elif 'hwloc' in self.spec.variants['affinity']:
            args.append('--enable-hwloc')
            args.append('--disable-capabilities')
        elif 'capabilities' in self.spec.variants['affinity']:
            args.append('--disable-hwloc')
            args.append('--enable-capabilities')

        # Dependency free flags specific to os=linux.  It don't see the value
        # in validating the os with `self.spec.satisfies('platform=linux')` and
        # seems better to let the user to decide what they want.
        if 'none' not in self.spec.variants['virt']:
            if 'openvz' in self.spec.variants['virt']:
                args.append('--enable-openvz')
            if 'ancient-vserver' in self.spec.variants['virt']:
                args.append('--enable-ancient-vserver')
                args.append('--enable-vserver')
            if 'vserver' in self.spec.variants['virt']:
                args.append('--enable-vserver')

        return args
