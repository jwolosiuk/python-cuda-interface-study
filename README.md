# python-cuda-interface-study

The goal of the project is to play around and create a simplistic boilerplate code for Python-C++ and Python-CUDA integrations.


- pip install .
```
In [1]: import cpp_bindings

In [2]: cpp_bindings.get_result()
Out[2]: 42

In [3]: import python_code

In [4]: python_code.get_result2()
Out[4]: 84
```


Todo:
- [x] builable C++ code
- [x] Python wrapper for the C++ code
- [x] setup.py for Python package
- [ ] simple and runable CUDA kernel
- [ ] Python wrapper and setup.py work with CUDA
- [ ] find a way to return GPU tensor from C++ directly to Python/pytorch (without copy to host)


Finally:
- [ ] simple API
- [ ] Dockerfile and docker-compose