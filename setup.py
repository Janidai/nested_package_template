import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-janid', # Replace with your own username e.g example-pkg-name
    version='0.0.1',
    author='janid',
    author_email='janid.abdellah@gmail.com',
    description='A small example of package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    license='',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",

    ],
    python_requires='>=3.6',
)
