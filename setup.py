#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-omx-macos',
    version='0.0.1',
    license='MIT',
    author='Oh My Xonsh',
    author_email='ohmyxonsh@gmail.com',
    description="macOS utilities for Oh-My-Xonsh.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/oh-my-xonsh/xontrib-omx-macos',
    project_urls={
        "Documentation": "https://github.com/oh-my-xonsh/xontrib-omx-macos/blob/master/README.md",
        "Code": "https://github.com/oh-my-xonsh/xontrib-omx-macos",
        "Issue tracker": "https://github.com/oh-my-xonsh/xontrib-omx-macos/issues",
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Unix Shell",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
