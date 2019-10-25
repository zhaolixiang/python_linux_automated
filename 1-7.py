import psutil
from subprocess import PIPE

# 通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的相关信息
p=psutil.Popen(["/usr/bin/python","-c","print('hello')"],stdout=PIPE)
print(p.name())
print(p.username())
print(p.communicate())
# 得到进程运行的CPU时间，更多方法见上一小节
# print(p.cpu_times())