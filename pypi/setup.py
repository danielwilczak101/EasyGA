from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='EasyGA',
    version='1.2.0',
    description='EasyGA is a python package designed to provide an easy-to-use Genetic Algorithm. The package is designed to work right out of the box, while also allowing the user to customize features as they see fit.',
    py_modules=["EasyGA","attributes","test_EasyGA","decorators"],
    packages=find_packages(where='EasyGA'),
    package_dir={
        '': 'EasyGA',
    },
    python_requires='>=3.6',
    url="https://github.com/danielwilczak101/EasyGA",
    author="Daniel Wilczak, Jack RyanNguyen, Ryley Griffith, Jared Curtis, Matthew Chase Oxamendi",
    author_email="danielwilczak101@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifier=[
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        ],
    install_requires = ["matplotlib ~= 3.3.2",
                        "pyserial ~= 3.4",
                        "pytest>=3.7",
                        "tabulate >=0.8.7"
                        ],
    )
