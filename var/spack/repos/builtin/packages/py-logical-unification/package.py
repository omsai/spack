# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLogicalUnification(PythonPackage):
    """Logical unification in Python, extensible via dispatch."""

    homepage = "http://github.com/pythological/unification/"
    pypi = "logical-unification/logical-unification-0.4.5.tar.gz"

    maintainers("omsai")

    version("0.4.5", sha256="7c6a6c1b7c6baa0f5b9af93f06cfc8d2419b6b793346b678ed1367c05ce74558")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-multipledispatch", type=("build", "run"))
    depends_on("py-toolz", type=("build", "run"))
