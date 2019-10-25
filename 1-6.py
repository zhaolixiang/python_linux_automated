import psutil

# 列出所有进程PID
print(psutil.pids())

# 实例化一个Process对象，参数为一个进行PID
p=psutil.Process(300)
print('进程名：',p.name())
print('进行bin路径：',p.exe())
print('进程工作目录绝对路径：',p.cwd())
print('进程状态：',p.status())
print('进程创建时间，时间戳格式：',p.create_time())
print('进程uid信息：',p.uids())
print('进程gid信息：',p.gids())
print('进程CPU时间信息，包括user、system两个CPU时间:',p.cpu_times())
# print('get进程CPU亲和度，如果设置进程CPU亲和度，将CPU号作为参数即可：',p.cpu_affinity())
print('进程内存利用率：',p.memory_percent())
print('进程内存rss、vms信息：',p.memory_info())
# print('进程IO信息，包括读写IO数及字节数',p.io_counters())
print('返回打开进程socket的namedutples列表，包括fs、family、laddr等信息',p.connections())
print('进程开启的线程数',p.num_threads())


