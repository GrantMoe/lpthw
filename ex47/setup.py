try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LPTHW Exercise 47',
    'author': 'Grant Moe',
    'url': 'https://github.com/GrantMoe/lpthw/ex47',
    'download_url': 'https://github.com/Grantmoe/lpthw',
    'author_email': 'Grant@GrantMoe.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)