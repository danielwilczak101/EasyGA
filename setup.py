from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='EasyGA',
    version='0.0.14',
    description='A ubiquitous or general purpuse GA',
    #py_modules=["EasyGA"],
    #package_dir={'':'src'},
    packages=find_packages(),
    py_modules=['src'],
    python_requires='>=3.6',
    url="https://github.com/danielwilczak101/EasyGA",
    author="Daniel Wilczak",
    author_email="danielwilczak101@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = ["blessings ~= 1.7",],
    )

