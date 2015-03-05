from distutils.core import setup, Extension
from os import getenv
import sys
import os
setup(
    name = "lpsolve55",
    version = "5.5.0.9",
    description = "Linear Program Solver, Interface to lpsolve",
    author = "Peter Notebaert",
    author_email = "lpsolve@peno.be",
    url = "http://www.peno.be/",
    py_modules=['lp_solve', 'lp_maker'],
    ext_modules = [
        Extension("lpsolve55",
        ["lpsolve.c", "pythonmod.c"],
        define_macros=[('PYTHON', '1'), ('NOWIN32', '1'), ('NODEBUG', '1'), ('DINLINE', 'static'), ('NONUMPY', '1'), ('_CRT_SECURE_NO_WARNINGS', '1')],
        libraries = ["lpsolve55_pic", "colamd"])
    ]
)
