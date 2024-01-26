#!/usr/bin/python3
import inspect
import string

source_code_replace = inspect.getsource(str.maketrans)
print(source_code_replace)
