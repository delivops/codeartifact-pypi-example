from setuptools import setup, find_packages
import os

# Get version from environment variable
VERSION = os.environ.get("VERSION")

setup(
    name="my-lib-1",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        # your dependencies here
    ],
    description="A simple example library",
    author="DelivOps",
)
