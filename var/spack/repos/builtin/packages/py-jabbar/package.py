# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJabbar(PythonPackage):
    """Just Another Beautiful progress BAR (some might replace Beautiful by
    Boring)."""

    homepage = "https://github.com/yannikschaelte/jabbar"

    pypi = "jabbar/jabbar-0.0.15.tar.gz"

    maintainers("omsai")

    version("0.0.15", sha256="7d152688432245c72b6986ff53c4ba1754cd462f5fb2f144e54a7e44a14a002c")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-wheel@0.36.2:", type="build")

    depends_on("py-setuptools@52:", type="build")
