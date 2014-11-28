import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='fontawesome-markdown',
      version='0.2.4',
      description='Font Awesome support for Markdown',
      long_description=readme(),
      url='http://bmcorser.github.com/fontawesome-markdown',
      author='bmcorser',
      author_email='bmcorser@gmail.com',
      license='GPL',
      packages=['fontawesome_markdown'],
      install_requires=['markdown'],
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.4',
      ])
