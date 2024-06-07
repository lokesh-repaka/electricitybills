# importing the libraries
from setuptools import find_packages,setup
from typing import List 
HYPHEN_E_DOT_REQUIREMENTS = '-e .'

def get_requirements(file_path:str) ->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT_REQUIREMENTS in requirements:
        requirements.remove(HYPHEN_E_DOT_REQUIREMENTS)



__version__="0.0.1"
SRC_REPO ="ElectricityBill"
setup(
    name = SRC_REPO,
    version=__version__,
    description="This is a project to predict household electricity bill",
    author="Lokesh",
    author_email="lokeshrepaka4@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')


)