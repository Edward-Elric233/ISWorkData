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

def dot2graph(input_filter, output_filter, file_name):
    print(input_filter)
    print(output_filter)
    print(file_name)
    lib.dot2graph(convert_type(input_filter), convert_type(output_filter), convert_type(file_name));

if __name__ == '__main__':
    #print("test")
    input_dir = "./dot/"
    output_dir = "./graph"
    file_name = "data1.json"
    if len(sys.argv) == 4:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        file_name = sys.argv[3]
    dot2graph(input_dir, output_dir, file_name)
