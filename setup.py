from setuptools import setup, find_packages


setup(
		name='ProgressBar',
		version='1.0',
		description='Simple progressbar utility.',
		author='Florian Lardeux',
		packages=find_packages(),
		python_requires='>3.7',
		install_requires=['numpy>=1.24']

		)