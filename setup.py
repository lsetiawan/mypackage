# This setup.py was autogenerated, please edit for further details
import os
from codecs import open

from setuptools import find_packages, setup

import versioneer

here = os.path.abspath(os.path.dirname(__file__))

# Dependencies.
with open('requirements.txt') as f:
    requirements = f.readlines()
install_requires = [t.strip() for t in requirements]

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='myscience',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='test package!!!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='john',
    author_email='john@example.com',
    maintainer='john',
    maintainer_email='john@example.com',
    python_requires='>=3',
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[],
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=['setuptools>=38.6.0', 
                    'wheel>=0.31.0', 
                    'twine>=1.11.0']
)
