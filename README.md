# Introduction
A template of a python project with nested packages.


# Project strcuture:

## Importing functions:

What is imported in ```__init__.py``` ; can be called using the dot notation when the directory is imported as
package.
for example, in the nested_pkg_1 directory we import ```nested_function()``` from ```nst_1.py```
in ```nested_pkg_1/__init__.py```
```
# nested_pkg_1/__init__.py
# Import functions from the modules in the package nested_pkg_1
from example_pkg.sub_pkg_1.nested_pkg_1.nst_1 import nested_function
```

## Importing modules:

## Importing packages:
Then in sub_pkg_1/__init__.py, Then we import the nested_pkg_1  
```
# Impost nested_pkg_1
from example_pkg.sub_pkg_1 import nested_pkg_1
```


When nested_pkg_1 package is imported, nested_function can be called from nested_pgk_1
in example_pkg/core.py
```
# from example_pkg import sub_pkg_1
sub_pkg_1.nested_pkg_1.nested_function()
```

# Testing


# References
- [Python Software Foundation [US]. (2017). Python Packaging User Guide Apr 03, 2020. https://packaging.python.org/](https://packaging.python.org/tutorials/packaging-projects/)
- [The Hitchhicker's Guide to Python](https://docs.python-guide.org/writing/structure/)

