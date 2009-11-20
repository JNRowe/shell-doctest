"""
Shell Doctest module.

:Copyright: (c) 2009, the Shell Doctest Team All rights reserved.
:license: BSD, see LICENSE for more details.
"""

from distutils.core import setup

if __name__ == "__main__":
    setup(
        name='shelldoctest',
        version='0.2',
        author='Takanao ENDOH',
        author_email='endoh@accense.com',
        maintainer='Takanao ENDOH',
        maintainer_email='djmchl@gmail.com',
        url='http://code.google.com/p/shell-doctest/',
        description='Doctest/UnitTest for shell',
        download_url='http://code.google.com/p/shell-doctest/',
        install_requires=[
            'setuptools',
            'commandlineapp',
            'paramiko',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: BSD License',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Programming Language :: Unix Shell',
            'Topic :: Software Development :: Testing',
        ],
        platforms='Any',
        license='New BSD License',
        packages=['shelldoctest'],
        scripts=['shell-doctest'],
    )

