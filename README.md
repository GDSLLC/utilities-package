# README

## requirements

This project expects to be run in a python 3.6 virtual env on ubuntu 16.04

## workflow

python setup.py register -r pypitest

python setup.py sdist upload -r pypitest

python setup.py register -r pypi

python setup.py sdist upload -r pypi
