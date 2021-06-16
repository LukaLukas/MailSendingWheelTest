from setuptools import setup

with open('requirements') as f:
    required = f.read().splitlines()

setup(name='dokr',
      version='0.1',
      # description='The funniest joke in the world',
      # url='http://github.com/storborg/funniest',
      # author='Luka Pavlica',
      # author_email='luka.pavlica93@gmail.com',
      # license='MIT',
      packages=['dokr',
                'dokr.firstfolder',
                ],
      install_requires=required,
      # zip_safe=False
)