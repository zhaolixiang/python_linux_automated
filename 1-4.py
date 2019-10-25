import psutil

# 使用psutil.net_io_counters获取网络总的IO信息、默认pernic=False
print(psutil.net_io_counters())

# 如果pernic=True，将输出每个网络接口的IO信息
print(psutil.net_io_counters(pernic=True))