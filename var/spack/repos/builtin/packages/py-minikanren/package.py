# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMinikanren(PythonPackage):
    """Logic/relational programming in Python with miniKanren."""

    homepage = "http://github.com/pythological/kanren"
    pypi = "miniKanren/miniKanren-1.0.3.tar.gz"

    maintainers("omsai")

    version("1.0.3", sha256="1ec8bdb01144ad5e8752c7c297fb8a122db920f859276d25a72d164e998d7f6e")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-cons@0.4.0:", type=("build", "run"))
    depends_on("py-etuples@0.3.0:", type=("build", "run"))
    depends_on("py-logical-unification@0.4.1:", type=("build", "run"))
    depends_on("py-multipledispatch", type=("build", "run"))
    depends_on("py-toolz", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
