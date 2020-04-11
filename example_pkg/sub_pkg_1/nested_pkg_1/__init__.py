# Title     : TODO
# Objective : TODO
# Created by: noonwave
# Created on: 4/11/20


# Import functions from the modules in the package
from example_pkg.sub_pkg_1.nested_pkg_1.nst_1 import nested_function

"""
What is imported in __init__ ; can be called using the dot notation when the directory in imported as
package.
for example, in the nested_pkg_1 directory we import nested_function() from nst_1.py
in nested_pkg_1/__init__.py
add:
"""
# # Import functions from the modules in the package
# from example_pkg.sub_pkg_1.nested_pkg_1.nst_1 import nested_function

"""
in sub_pkg_1/__init__.py, Then we import the nested_pkg_1  
"""
# # Impost nested packages
# from example_pkg.sub_pkg_1 import nested_pkg_1
"""
When nested_pkg_1 package is imported, nested_function can be called from nested_pgk_1
in example_pkg/core.py
"""
# from example_pkg import sub_pkg_1
# sub_pkg_1.nested_pkg_1.nested_function()
