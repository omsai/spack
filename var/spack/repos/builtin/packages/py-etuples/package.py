# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEtuples(PythonPackage):
    """Python S-expression emulation using tuple-like objects."""

    homepage = "http://github.com/pythological/etuples"
    pypi = "etuples/etuples-0.3.8.tar.gz"

    maintainers("omsai")

    version("0.3.8", sha256="babb99e09428e7985d2baf5537f38ca1e47b596e1fadbef7db12388cab0a92de")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-cons", type=("build", "run"))
    depends_on("py-multipledispatch", type=("build", "run"))
