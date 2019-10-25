import psutil,datetime

# 使用psutil.users方法返回当前登录系统的用户信息
print(psutil.users())

# 使用psutil.boot_time方法获取开机时间，以Linux时间戳格式返回
print(psutil.boot_time())

print('开机时间：',datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%s'))