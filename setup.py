import io
from setuptools import setup, find_packages

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='BellowAveragePythonUtilities',
    version='0.1.0',
    packages=['openai_api'],
    install_requires=["openai==0.28"],
    description='A simple API for Python APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BellowAverage/PythonUtilities',
    author='Chris Wang',
    author_email='chriswang2025@u.northwestern.edu',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
