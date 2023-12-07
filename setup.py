from setuptools import setup,find_packages
from typing import List

def get_req(filepath):
    requirements=[]
    with open(filepath) as obj:
        requirements=obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
name='Healthcare ML project',
version='0.0.1',
author='Chirag',
author_email='mahajan.chirag3@gmail.com',
packages=find_packages(),
install_requires=get_req("requirements.txt")

)


