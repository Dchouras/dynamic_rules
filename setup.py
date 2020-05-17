import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamic-rules-dchouras",
    version="0.0.1",
    author="Devesh Chourasiya",
    author_email="devesh.cs@gmail.com",
    description="Dynamic Rule Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dchouras/dynamic_rules",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
