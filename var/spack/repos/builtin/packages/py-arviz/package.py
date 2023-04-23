# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyArviz(PythonPackage):
    """ArviZ (pronounced "AR-vees") is a Python package for exploratory
    analysis of Bayesian models. Includes functions for posterior analysis,
    model checking, comparison and diagnostics."""

    homepage = "https://github.com/arviz-devs/arviz"
    pypi = "arviz/arviz-0.6.1.tar.gz"

    version("0.15.0", sha256="80961e4552680758a2049ca0adcdb02ae8e1f3e7ce57f410f0a778dcefe027e3")

    depends_on("python@3.8:", when="@0.13.0:", type=("build", "run"))
    depends_on("py-setuptools@60.0:", type="build")

    # requirements.txt
    depends_on("py-matplotlib@3.2:", type=("build", "run"))
    depends_on("py-h5netcdf@1.0.2:", type=("build", "run"))
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pandas@1.4.0:", type=("build", "run"))
    depends_on("py-scipy@1.8.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.1.0:", type=("build", "run"))
    depends_on("py-xarray-einstats@0.3:", type=("build", "run"))
    depends_on("py-xarray@0.21:", type=("build", "run"))

    # requirements-test.txt
    depends_on("py-pytest", type="test")
    depends_on("py-pytest-cov", type="test")
    depends_on("py-cloudpickle", type="test")
    # requirements-optional.txt
    depends_on("py-numba", type="test")
    depends_on("py-netcdf4", type="test")
    depends_on("py-bokeh@1.4.0:2", type="test")
    depends_on("py-contourpy", type="test")
    depends_on("py-ujson", type="test")
    depends_on("py-dask +distributed", type="test")
    depends_on("py-zarr@2.5.0:", type="test")
