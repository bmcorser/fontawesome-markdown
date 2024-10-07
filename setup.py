import sys
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='fontawesome-in-markdown',
    version='0.1.1',
    description='Markdown extension to include FontAwesome icons with ease.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='http://stickgrinder.github.com/fontawesome-in-markdown',
    author='StickGrinder',
    author_email='stickgrinder@gmail.com',
    license='GPL-3.0',
    packages=['fontawesome_in_markdown'],
    package_dir={'fontawesome_in_markdown': 'src/fontawesome_in_markdown'},
    install_requires=['markdown'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    test_suite='tests',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)