# Package Imports
from setuptools import find_packages, setup

setup(
	name="hangingart",
	version="0.1.0",
	author="Ian Davies",
	url="https://github.com/IanRichardDavies/HangingArt",
	description="Python tool to help decorate a house with art",
	package_data={"": ["metadata/*"],},
	packages=find_packages(),
	tests_require=["pytest",],
	)