# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyH5netcdf(PythonPackage):
    """A Python interface for the netCDF4 file-format that reads and writes local or
    remote HDF5 files directly via h5py or h5pyd, without relying on the Unidata netCDF
    library."""

    homepage = "https://github.com/h5netcdf/h5netcdf"
    pypi = "h5netcdf/h5netcdf-0.10.0.tar.gz"

    version("1.1.0", sha256="932c3b573bed7370ebfc9e802cd60f1a4da5236efb11b36eeff897324d76bf56")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")

    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
