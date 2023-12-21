import ctypes
from numpy.ctypeslib import ndpointer

lib = ctypes.CDLL("./tester.so")
lib.test_array.restype = ndpointer(dtype=ctypes.c_int, shape=(2,))

res = lib.test_array()
print(res)
