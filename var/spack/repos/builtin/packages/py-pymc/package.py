# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymc(PythonPackage):
    """PyMC (formerly PyMC3) is a Python package for Bayesian statistical
    modeling and Probabilistic Machine Learning focusing on advanced Markov
    chain Monte Carlo (MCMC) and variational inference (VI) algorithms. Its
    flexibility and extensibility make it applicable to a large suite of
    problems."""

    homepage = "https://github.com/pymc-devs/pymc"
    pypi = "pymc/pymc-5.0.2.tar.gz"

    maintainers("omsai")

    version("5.0.2", sha256="932439f1c9276029d874360bb1258cb67d4d29349b4ba4e8f9c09517f6b558ad")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-arviz@0.13.0:", type=("build", "run"))
    depends_on("py-cachetools@4.2.1:", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
    depends_on("py-fastprogress@0.2.0:", type=("build", "run"))
    depends_on("py-numpy@1.15.0:", type=("build", "run"))
    depends_on("py-pandas@0.24.0:", type=("build", "run"))
    depends_on("py-pytensor@2.9.1:", type=("build", "run"))
    depends_on("py-scipy@0.18.1:", type=("build", "run"))
    depends_on("py-typing-extensions@3.7.4:", type=("build", "run"))

    # setup.py
    depends_on("py-pytest", type="test")
    depends_on("py-pytest-cov", type="test")
