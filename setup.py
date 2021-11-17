from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sourcerers/__init__.py
from sourcerers import __version__ as version

setup(
	name="sourcerers",
	version=version,
	description="This app will be used to develop freight forwarding module, for now it will focus on Indian Freight Forwarding Industry",
	author="Himanshu",
	author_email="himanshuu@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
