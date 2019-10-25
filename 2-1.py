from IPy import IP
#4代表IPv4类型
print(IP('10.0.0.0/8').version())
# 6代表IPv6类型
print(IP('::1').version())