from setuptools import setup, find_packages

setup(
	name="reginafolder", 
	packages=find_packages(),
	install_requires=['setuptools'],#, 'pos >= v2.1.0'],
	python_requires='>=3.5',
	entry_points={
			'console_scripts': [
				'reginafolder=reginafolder.main:main'
							   ]
				 }
	)