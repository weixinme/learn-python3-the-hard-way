try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Wei Xin',
    'url': 'URL to get it at. ',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)