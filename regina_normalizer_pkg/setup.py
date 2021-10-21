from setuptools import setup, find_packages

setup(
	name="regina-normalizer", 
	packages=find_packages(),
	install_requires=['setuptools'],#, 'pos >= v2.1.0'],
	python_requires='>=3.5',
	entry_points={
			'console_scripts': [
				'regina_normalizer=regina_normalizer.main:main'
							   ]
				 }
	)