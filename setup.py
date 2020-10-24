from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='EasyGA',
    version='0.0.27',
    description='A ubiquitous or general purpuse GA',
    py_modules=["EasyGA","attributes","test_EasyGA"],
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
    extra_require = {
        "dev": [
            "pytest>=3.7",
            ],
        },
    )
