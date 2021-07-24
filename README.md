# 数据建模模块
## 使用方法
- 命令行调用：
    ```shell
    python3 data_process.py "输入文件路径" "输出文件路径"
    python3 data_process.py "./dot/data1.json" "./graph/data1.json"
    ```
- 代码设置：在`data_process.py`文件中，通过设置`input_path`、`output_path`两个变量的值设定输入文件路径、输出文件路径

## 实现原理
核心算法使用C++进行编码后编译成动态库`libcppdeal.so`，然后使用python导入该动态库
编译动态库的命令：
```shell
g++ -shared -Wl,-soname,test -o libcppdeal.so -fPIC data_process.cpp -std=c++11
```

## 注意事项
必须将动态库`libcppdeal.so`和脚本`data_process.py`放到同一个目录下