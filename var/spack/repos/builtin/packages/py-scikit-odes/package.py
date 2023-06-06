# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitOdes(PythonPackage):
    """Odes is a scikit toolkit for scipy to add extra ode solvers.
    Specifically it interfaces the Sundials solvers cvode, cvodes, ida and
    idas.  It this way it provides extra modern ode and dae solvers you can
    use, extending the capabilities offered in scipy.integrade.ode."""

    homepage = "https://github.com/bmcage/odes"

    pypi = "scikits.odes/scikits.odes-2.7.0.tar.gz"
    github = "https://github.com/bmcage/odes.git"

    maintainers("omsai")

    version("2.7.0", sha256="a71e19e1485893754ae8c050668232fcc694f17b83602e75fbebf7bf9f975e1e")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools@:64.0.0", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython@:3.0.0a7", type=("build", "run"))
    depends_on("sundials@6:")

    def setup_run_environment(self, env):
        env.set("SUNDIALS_INST", self.spec["sundials"].prefix)
