from setuptools import setup, find_packages

setup(
    name='Thermo atum',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'openpyxl'
    ]
)