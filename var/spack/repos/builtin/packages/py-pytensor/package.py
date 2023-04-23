# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytensor(PythonPackage):
    """PyTensor is a fork of Aesara - a Python library that allows one to
    define, optimize, and efficiently evaluate mathematical expressions
    involving multi-dimensional arrays."""

    homepage = "https://github.com/pymc-devs/pytensor"
    pypi = "pytensor/pytensor-2.9.1.tar.gz"

    maintainers("omsai")

    version("2.10.1", sha256="6fc96a75cf5348e89f4f44927c585f6f0059c4ab61282564864f67437557bd7c")
    version("2.9.1", sha256="b5a50203dd247ab887929adcfe2f812624e3ce07821fe530fdfc1ed553abbb58")

    variant("jax", default=True)

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools@48:", type="build")

    depends_on("py-cython", type=("build", "run"))
    depends_on("py-numpy@1.17.0:", type=("build", "run"))
    depends_on("py-versioneer@0.28: +toml", type=("build", "run"))

    depends_on("py-cons", type="run")
    depends_on("py-etuples", type="run")
    depends_on("py-filelock", type="run")
    depends_on("py-logical-unification", type="run")
    depends_on("py-minikanren", type="run")
    depends_on("py-scipy@0.14:", type="run")
    depends_on("py-typing-extensions", type="run")

    depends_on("py-jax", when="+jax", type="run")
    depends_on("py-jaxlib", when="+jax", type="run")
