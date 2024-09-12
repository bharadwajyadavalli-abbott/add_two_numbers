from setuptools import setup, find_packages

setup(
    name='add_two_numbers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='Bharadwaj Yadavalli',
    author_email='bharadwaj.yadavalli@abbott.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bharadwajyadavalli-abbott/add_two_numbers',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
