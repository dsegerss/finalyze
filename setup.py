"""Build and install Finalyze."""

import os

from setuptools import Extension, find_packages, setup

setup(
    name="finalyze",
    version="0.2.0.dev1",
    description="An experimental stock market analysis and prediction sandbox",
    url="https://github.com/dsegerss/finalyze",
    author="David Segersson",
    author_email="david.segersson@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Internet :: WSGI :: Application",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "sqlalchemy",
        "pandas",
        "yfinance",
        "psycopg2-binary"
    ],
)
