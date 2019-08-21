from setuptools import setup

install_requires = [
    'pandas>=0.25.0',
    'numpy>=1.15.4',
    'functools']

setup(name='misha_math',
      version='0.0.1',
      description='test',
      author='Misha Berrien',
      install_requires=install_requires,
      author_email='misha.berrien@gmail.com',
      packages=['mypackage_one', 'mypackage_two'])
