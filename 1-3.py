import psutil

# 使用psutil.disk_partitions 方法获取磁盘完整信息
print(psutil.disk_partitions())

# 使用psutil.disk_usage方法获取分区(参数的使用情况)
print(psutil.disk_usage('/'))

# 使用psutil.disk_io_counters获取硬盘的IO个数、读写信息
print(psutil.disk_io_counters())

# 如果disk_io_counters传递参数：perdisk=True,
# 就表示获取单个分区IO个数、读写信息
print(psutil.disk_io_counters(perdisk=True))