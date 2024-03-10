from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in confederate/__init__.py
from confederate import __version__ as version

setup(
	name="confederate",
	version=version,
	description="App for Chart of accounts company",
	author="Safeer C P",
	author_email="erpconfederate@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
