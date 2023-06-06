# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyabc(PythonPackage):
    """Massively parallel, distributed and scalable ABC-SMC (Approximate
    Bayesian Computation - Sequential Monte Carlo) for parameter estimation of
    complex stochastic models. Provides numerous state-of-the-art algorithms
    for efficient, accurate, robust likelihood-free inference, described in the
    documentation and illustrated in example notebooks. Written in Python with
    support for especially R and Julia."""

    homepage = "https://github.com/icb-dcm/pyabc"
    pypi = "pyabc/pyabc-0.12.10.tar.gz"
    git = "https://github.com/icb-dcm/pyabc.git"

    maintainers("omsai")

    version("main", branch="main")
    version("0.12.10", sha256="038c94894b3e4d74229f74b50872a5811303c855f28c9581d722fd30cc0fbe32")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-wheel@0.36.2:", type="build")

    depends_on("py-setuptools@52:", type="build")

    depends_on("py-numpy@1.19.1:", type=("build", "run"))
    depends_on("py-scipy@1.5.2:", type=("build", "run"))
    depends_on("py-pandas@2.0.1:", type=("build", "run"))
    depends_on("py-cloudpickle@1.5.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.23.1:", type=("build", "run"))
    depends_on("py-click@7.1.2:", type=("build", "run"))
    depends_on("py-redis@2.10.6:", type=("build", "run"))
    depends_on("py-distributed@2022.10.2:", type=("build", "run"))
    depends_on("py-matplotlib@3.3.0:", type=("build", "run"))
    depends_on("py-sqlalchemy@2.0.12:", type=("build", "run"))
    depends_on("py-jabbar@0.0.10:", type=("build", "run"))
    depends_on("py-gitpython@3.1.7:", type=("build", "run"))
