import psutil

# 使用psutil.virtual_memory()方法获取内存完整信息
mem=psutil.virtual_memory()
print(mem)
# 获取内存个数
print('内存个数：',mem.free)
# 获取SWAP分区信息
print('SWAP分区信息：',psutil.swap_memory())