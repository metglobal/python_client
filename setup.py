# coding: utf-8

"""
    Hotelspro Api Client

    Hotelspro Api Client

    OpenAPI spec version: 2.0.0
    Contact: clientintegration@hotelspro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Hotelspro Api Client",
    author_email="clientintegration@hotelspro.com",
    url="",
    keywords=["Swagger", "Hotelspro Api Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Hotelspro Api Client
    """
)