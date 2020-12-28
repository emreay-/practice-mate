
from setuptools import setup, find_packages

setup(
    name="practice_mate",
    version="0.1.0",
    description="A guitar practice tool to improve theory and keyboard navigation",
    author="Emre Ay",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[]
)
