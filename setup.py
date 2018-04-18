try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A simple countdown program that plays an alarm at the end of the countdown.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Simple Countdown Program'
}

setup(**config)