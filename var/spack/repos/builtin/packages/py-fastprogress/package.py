# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFastprogress(PythonPackage):
    """A fast and simple progress bar for Jupyter Notebook and
    console. Created by Sylvain Gugger for fast.ai."""

    homepage = "https://github.com/fastai/fastprogress"
    pypi = "fastprogress/fastprogress-1.0.0.tar.gz"

    version("1.0.3", sha256="7a17d2b438890f838c048eefce32c4ded47197ecc8ea042cecc33d3deb8022f5")
    version("1.0.0", sha256="89e28ac1d2a5412aab18ee3f3dfd1ee8b5c1f2f7a44d0add0d0d4f69f0191bfe")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
