#!/usr/bin/env python
# coding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epd-library",
    version="0.1.2",
    author="t4skforce",
    author_email="7422037+t4skforce@users.noreply.github.com",
    description="GDEP015OC1 e-paper for raspberry pi (Waveshare 1.54inch e-paper)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t4skforce/epd-library-python",
    entry_points={'console_scripts': [
        'epd1in54=epd1in54.__main__:main',
        'epd1in54b=epd1in54b.__main__:main',
        'epd1in54c=epd1in54c.__main__:main',
        'epd2in7=epd2in7.__main__:main',
        'epd2in7b=epd2in7b.__main__:main',
        'epd2in9=epd2in9.__main__:main',
        'epd2in9b=epd2in9b.__main__:main',
        'epd2in13=epd2in13.__main__:main',
        'epd2in13b=epd2in13b.__main__:main',
        'epd4in2=epd4in2.__main__:main',
        'epd4in2b=epd4in2b.__main__:main',
        'epd7in5=epd7in5.__main__:main',
        'epd7in5b=epd7in5b.__main__:main',
    ]},
    packages=setuptools.find_packages(),
    install_requires=[
        'Pillow>=6.1.0',
        'RPi.GPIO>=0.6.5',
	'spidev>=3.4'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)