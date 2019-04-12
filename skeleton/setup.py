try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MY PROJECT',
    'author': 'Grant Moe',
    'url': 'https://github.com/GrantMoe/MY_PROJECT_NAME',
    'download_url': 'https://github.com/Grantmoe/MY_PROJECT_NAME?',
    'author_email': 'Grant@GrantMoe.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'PROJECTNAME'
}

setup(**config)