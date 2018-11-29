#Python wrapper for the visualizer
from os import path
import ctypes


# ============ Load the C library
full_path_to_lib = path.join(path.dirname(path.realpath(__file__)), '../bin/libmj_viz.so')
print(full_path_to_lib)
lib = ctypes.CDLL(full_path_to_lib)


# ============ Prepare the info structure
class vizModelInfo(ctypes.Structure):
    _fields_ = [
        ("nq", ctypes.c_int),
        ("nv", ctypes.c_int),
        ("nu", ctypes.c_int),
        ("na", ctypes.c_int)]
def printStructure(o):
    for field_name, field_type in o._fields_:
        print('%s: %s' % (field_name, getattr(o, field_name)))


# ============ Define a special type for the 'double *' argument
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)

    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    # Cast from lists/tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    # Cast from a numpy array
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


# ============ Initialize the viz  
# void viz_init(char* modelPath, char* licensePath);
_viz_init = lib.viz_init
_viz_init.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
_viz_init.restype = None
def viz_init(modelPath, licensePath):
    return _viz_init(modelPath.encode('utf-8'), licensePath.encode('utf-8'))


# ============ Close the viz
# void viz_close();
_viz_close = lib.viz_close
def viz_close():
    _viz_close()


# ============ Update the visualizer's state
# bool viz_update(double *time, double *qpos, double *qvel, int nq, int nv);
_viz_update = lib.viz_update
_viz_update.argtypes = [ctypes.c_double, DoubleArrayType(), DoubleArrayType(), ctypes.c_int, ctypes.c_int]
_viz_update.restype = ctypes.c_bool
def viz_update(time, qpos, qvel):
    _viz_update(time, qpos.copy(), qvel.copy(), len(qpos), len(qvel))


# ===== get the model info
# bool viz_model_info(vizModelInfo *info);
_viz_model_info = lib.viz_model_info
_viz_model_info.argtypes = (ctypes.POINTER(vizModelInfo),) # the terminating "," is important. It wasted my 2 hours :(
_viz_model_info.restype = ctypes.c_bool
def viz_model_info():
    info = vizModelInfo()
    _viz_model_info(info)
    return info
