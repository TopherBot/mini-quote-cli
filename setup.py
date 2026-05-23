from setuptools import setup, find_packages

setup(
    name='mini-quote-cli',
    version='0.1.0',
    description='Tiny CLI that prints a random motivational quote',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'mini-quote-cli=mini_quote:main',
        ],
    },
    python_requires='>=3.8',
    license='MIT',
)