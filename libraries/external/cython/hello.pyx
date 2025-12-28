"""Cython hello world module."""

cpdef void hello():
    cdef str message = 'Hello World!'
    print(message)

