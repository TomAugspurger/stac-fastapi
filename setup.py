"""arturo-stac-api."""
import os
from imp import load_source

from setuptools import find_packages, setup

with open("README.md") as f:
    desc = f.read()

# Get version from stac-fastapi-api
__version__ = load_source(
    "stac_fastapi.api.version",
    os.path.join(
        os.path.dirname(__file__), "stac_fastapi_api/stac_fastapi/api/version.py"
    ),
).__version__  # type:ignore

install_requires = ["stac-fastapi-api", "stac-fastapi-extensions"]

extra_reqs = {
    "sqlalchemy": ["stac-fastapi-sqlalchemy"],
    "dev": ["pytest", "pytest-cov", "pytest-asyncio", "pre-commit", "requests"],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
}


setup(
    name="stac-fastapi",
    description="An implementation of STAC API based on the FastAPI framework.",
    long_description=desc,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author=u"Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/stac-fastapi",
    license="MIT",
    packages=find_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)
