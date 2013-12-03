from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='fontawesome-markdown',
      version='0.2',
      description='Font Awesome support for Markdown',
      long_description=readme(),
      url='http://bmcorser.github.com/fontawesome-markdown',
      author='bmcorser',
      author_email='benmarshallcorser@gmail.com',
      license='GPL',
      packages=['fontawesome_markdown'],
      install_requires=['markdown'],
      zip_safe=False)
