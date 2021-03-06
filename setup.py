from setuptools import setup

import sys
import os

version = '0.0.1'

long_description = open('README.md').read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='shopyangu_comm',
    version=version,
    packages=['shopyangu_comm'],
    description='Official Shopyangu\'s comm Python SDK',
    data_files=[('', ['README.md'])],
    license='MIT',
    author='Shopyangu',
    install_requires=[
        'requests>=v2.18.4',
        'schema>=0.6.7'
    ],
    python_requires=">=2.7.10",
    author_email='joe@shopyangu.com',
    url='https://github.com/Shopyangu-engineering/shopyangu_comm-python',
    download_url='https://codeload.github.com/Shopyangu-engineering/shopyangu_comm-python/tar.gz/' + version,
    keywords='voice sms whatsapp telegram airtime shopyangu',
    classifiers=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)