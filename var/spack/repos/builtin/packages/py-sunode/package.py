# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySunode(PythonPackage):
    """Python wrapper of sundials for solving ordinary differential
    equations."""

    homepage = "https://github.com/pymc-devs/sunode"
    url = "https://github.com/pymc-devs/sunode/archive/refs/tags/v0.4.0.tar.gz"

    maintainers("omsai")

    version("0.4.0", sha256="7c82b3872625052e537fe8099f69bf3b73169e8d560e2f07de7d9103753d1cbc")

    depends_on("py-setuptools", type="build")

    depends_on("py-cffi@1.0.0:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))

    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
