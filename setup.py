from setuptools import find_packages, setup

requirements = [
  'selenium',
  'Flask'
]

setup(
  name='',
  version='0.1',
  packages=find_packages(),
  install_requires=requirements,
  zip_safe=False
)
