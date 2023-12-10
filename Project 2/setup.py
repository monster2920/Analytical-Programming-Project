from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    author='Sandeep Varma Uppalapati',
    author_email='suppalap@mail.yu.edu',
    description="A package for extracting and analyzing web data",
    long_description_content_type="text/markdown",
    url='https://github.com/monster2920/Analytical-Programming-Project/tree/main/Project%202',
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "beautifulsoup4>=4.9.3",
    ],
)
