from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
	name="regina-normalizer",
	version="0.0.6",
	author = "Helga Svala Sigurðardóttir, Anna Björk Nikulásdóttir",
	author_email = "helgas@ru.is",
	url="https://github.com/cadia-lvl/regina-normalizer/tree/master/regina_package",
	description = "A text normalization package for Icelandic",
	license="MIT",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	packages=find_packages(),
	package_data={"": ["*.txt"]},
	include_package_data=True,
	install_requires=['setuptools', 'pos >= v2.1.0', 'wandb'],
	python_requires='>=3.5',
	entry_points={
			'console_scripts': [
				'regina_normalizer=regina_normalizer.main:main'
							   ]
				 }
	)
