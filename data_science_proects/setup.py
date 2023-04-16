from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        this functions wil return the list of packages to install from requirements.txt file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='data_science_proect',
    version='0.0.1',
    author='Mayank Tripathi',
    author_email='mayanktripathi4u@gmail.com',
    packages=find_packages(),
    # install_reqires=['pandas', 'numpy', 'seaborn'],
    install_reqires=get_requirements('requirements.txt')
)