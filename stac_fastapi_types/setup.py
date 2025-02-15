"""stac-fastapi api submodule."""
import os
from glob import glob
from imp import load_source
from os.path import basename, splitext

from setuptools import find_namespace_packages, setup

name = "stac-fastapi-types"
description = "Shared types for fastapi-stac, contains abstract base classes for implementing STAC backends."

__version__ = load_source(
    "stac_fastapi.types.version",
    os.path.join(os.path.dirname(__file__), "stac_fastapi/types/version.py"),
).__version__  # type:ignore

install_requires = [
    "attrs",
    "fastapi",
    "pydantic[dotenv]",
    "stac-pydantic==1.3.8",
]

with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
) as readme_file:
    readme = readme_file.read()

setup(
    name=name,
    description=description,
    version=__version__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=u"Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/stac-fastapi.git",
    packages=find_namespace_packages(),
    py_modules=[splitext(basename(path))[0] for path in glob("stac_fastapi/*.py")],
    include_package_data=False,
    install_requires=install_requires,
    license="MIT",
    keywords=["stac", "fastapi", "imagery", "raster", "catalog", "STAC"],
)
