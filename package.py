# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MetaBrainscales(Package):
    """Core package that contains dependencies of the core DLS software
    ONLY!"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    # PPU compiler dependencies
    depends_on('gettext')
    depends_on('zlib')
    depends_on('bison')
    depends_on('flex')
    depends_on('m4')
    depends_on('texinfo')
    depends_on('wget')
    conflicts('flex', when='@2.6.3', msg='Binutils 2.25 for Nux doesn\'t build with flex 2.6.3.')

    # host software dependencies
    depends_on('bitsery')
    depends_on('binutils+gold+ld+plugins') # specialize
    depends_on('boost@1.69.0: +graph+icu+mpi+python+numpy+coroutine+context cxxstd=17') # specialize boost (non-clingo)
    depends_on('cereal')
    depends_on('cppcheck')
    depends_on('doxygen+graphviz')
    depends_on('genpybind@ebrains')
    depends_on('gflags')
    depends_on('googletest@1.11.0: +gmock') # variadic templates needed
    depends_on('intel-tbb')  # ppu gdbserver
    depends_on('libelf')
    depends_on('liblockfile')
    depends_on('llvm')
    depends_on('log4cxx')
    depends_on('pkg-config')
    depends_on('python@3.7.0:') # BrainScaleS(-2) only supports Python >= 3.7
    depends_on('py-h5py') # PyNN tests need it
    depends_on('py-matplotlib')
    depends_on('py-nose')
    depends_on('py-numpy')
    depends_on('py-pybind11')
    depends_on('py-pybind11-stubgen')
    depends_on('py-pycodestyle')
    depends_on('py-pyelftools')
    depends_on('py-pylint')
    depends_on('py-pynn@0.9.4:')
    depends_on('py-pyyaml')
    depends_on('py-scipy')
    depends_on('py-sqlalchemy')
    depends_on('util-linux')
    depends_on('yaml-cpp+shared')

    depends_on('neuron')
    #depends_on('efel') pypi
    #depends_on('sciunit')
    depends_on('py-scipy')
    depends_on('py-numpy')
    depends_on('py-matplotlib')
    depends_on('py-quantities')
    #depends_on('collections')
    depends_on('py-multiprocess')
    #depends_on('functools')
    #depends_on('json')
    #depends_on('pickle')
    depends_on('gzip')
    #depends_on('copy_reg')
    depends_on('nest')
    depends_on('nest+mpi')
    depends_on('py-neo')

    # dummy installer; it's a "meta" package
    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        install(__file__, join_path(prefix.etc, spec.name + '.py'))
