import psutil

mem=psutil.virtual_memory()
print(mem.total,mem.used)

# 使用cpu_times方法获取CPU完整信息，
# 如果需要显示所有逻辑CPU信息，指定方法变量percpu=True即可
print(psutil.cpu_times())
print(psutil.cpu_times(percpu=True))
print('*'*30)
# 获取单项数据信息，如用户user的CPU时间比
print(psutil.cpu_times().user)
# 获取CPU的逻辑个数，默认logical=True
print('CPU逻辑个数：',psutil.cpu_count())
print('CPU物理个数：',psutil.cpu_count(logical=False))


