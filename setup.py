from setuptools import setup

setup(name='epd2in13',
      version='0.1.2',
      description='2.13inch e-Paper HAT - Implements for e-paper library',
      url='https://github.com/t4skforce/edp2in13',
      author='Yehui from Waveshare',
      author_email='service@waveshare.com',
      license='GPL',
      packages=['epd2in13'],
      install_requires=[
          'RPi.GPIO',
          'epdif',
          'Pillow'
      ],
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
      ],
      zip_safe=False)
