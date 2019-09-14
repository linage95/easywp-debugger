# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name='easywp-cron',
    version='2.2.0',
    description='EasyWP Cron REST API',
    url='https://github.com/SolidAlloy/easywp-debugger',
    author='Artem Perepelitsa',
    author_email='perepelartem@gmail.com',
    license='GNU',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='cron rest easywp debugger',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['alembic',
                      'Flask',
                      'Flask-Caching',
                      'Flask-Mail',
                      'Flask-Migrate',
                      'Flask-SQLAlchemy',
                      'Flask-SSLify',
                      'PyMySQL',
                      'python-dotenv',
                      'requests',
                      ],
)
