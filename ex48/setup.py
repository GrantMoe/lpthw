try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learning Python the Hard Way Exercise 48',
    'author': 'Grant Moe',
    'url': 'https://github.com/GrantMoe/lpthw/ex48',
    'download_url': 'https://github.com/Grantmoe/lpthw',
    'author_email': 'Grant@GrantMoe.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'Exercise 48'
}

setup(**config)