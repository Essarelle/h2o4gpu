from ctypes import *
from h2o4gpu.types import *
from h2o4gpu.libs.utils import cpu_lib_path

lib_path = cpu_lib_path()

try:
    h2o4gpuGLMCPU = cdll.LoadLibrary(lib_path)
    h2o4gpuGLMCPU.make_ptr_double.argtypes = [c_int, c_int, c_int, c_size_t, c_size_t, c_size_t, c_int,
                                               c_double_p, c_double_p, c_double_p, c_double_p, c_double_p,
                                               c_void_pp, c_void_pp, c_void_pp, c_void_pp, c_void_pp]
    h2o4gpuGLMCPU.make_ptr_double.restype = c_int

    h2o4gpuGLMCPU.make_ptr_float.argtypes = [c_int, c_int, c_int, c_size_t, c_size_t, c_size_t, c_int,
                                              c_float_p, c_float_p, c_float_p, c_float_p, c_float_p,
                                              c_void_pp, c_void_pp, c_void_pp, c_void_pp, c_void_pp]
    h2o4gpuGLMCPU.make_ptr_float.restype = c_int
except:
    print('\nWarning: H2O4GPU Elastic Net CPU shared object (dynamic library) not found at ' + lib_path)
    h2o4gpuGLMCPU = None
