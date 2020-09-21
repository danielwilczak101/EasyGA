from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='EasyGA',
    version='0.0.8',
    description='A ubiquitous or general purpuse GA',
    py_modules=["EasyGA"],
    package_dir={'':'src'},
    python_requires='>=3.6',
    url="https://github.com/danielwilczak101/EasyGA",
    author="Daniel Wilczak",
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
    install_requires = ["blessings ~= 1.7",
                        ],
    extra_require = {
        "dev": [
            "pytest>=3.7",
            ],
        },
    )
