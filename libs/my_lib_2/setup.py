from setuptools import setup, find_packages
import os

# Get version from environment variable
VERSION = os.environ.get("VERSION")

setup(
    name="my-lib-2",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        # your dependencies here
    ],
    description="Another simple example library",
    author="DelivOps",
)
