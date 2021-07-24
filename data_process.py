import ctypes
import sys

lib = ctypes.cdll.LoadLibrary("./libcppdeal.so");

lib.dot2graph.restype = ctypes.c_void_p;

#将python类型转换成c类型，支持int, float,string的变量和数组的转换
def convert_type(input, null=None):
    ctypes_map = {int:ctypes.c_int,
              float:ctypes.c_double,
              str:ctypes.c_char_p
              }
    input_type = type(input)
    if input_type is list:
        length = len(input)
        if length==0:
            print("convert type failed...input is "+input)
            return null
        else:
            arr = (ctypes_map[type(input[0])] * length)()
            for i in range(length):
                arr[i] = bytes(input[i],encoding="utf-8") if (type(input[0]) is str) else input[i]
            return arr
    else:
        if input_type in ctypes_map:
            return ctypes_map[input_type](bytes(input,encoding="utf-8") if type(input) is str else input)
        else:
            print("convert type failed...input is "+input)
            return null

def dot2graph(input_path, output_path):
    lib.dot2graph(convert_type(input_path), convert_type(output_path));

if __name__ == '__main__':
    input_path = "./dot/data1.json"
    output_path = "./graph/data1.json"
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    dot2graph(input_path, output_path)


