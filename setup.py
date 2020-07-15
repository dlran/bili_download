# coding: utf-8
import setuptools
import re
import os


__version__ = ''
thelibFolder = os.path.dirname(os.path.realpath(__file__))
with open(thelibFolder + '/bld/__version__.py') as f:
    __version__ = re.findall(r'__version__ = "(.+?)"', f.read())[0]

setuptools.setup(
  name='bld',
  version=__version__,
  author='dlr',
  author_email='dlr@yy.com',
  description=u'Bilibili downloader',
  packages=setuptools.find_packages(),
  url='https://dlr.com',
  entry_points={
    'console_scripts': [
      'bld=bld.cli:main'
    ]
  },
  install_requires=["ffd==0.0.7"],
  dependency_links=["git+https://github.com/dlran/ffd.git/@master#egg=ffd-0.0.7"],
  classifiers=[
      'Programming Language :: Python :: 3 :: Only'
  ]
)
