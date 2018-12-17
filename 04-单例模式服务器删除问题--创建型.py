class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []               # 装服务器的列表 要实现监控列表的动态

    def add_server(self):
        self._servers.append('Server 1')
        self._servers.append('Server 2')
        self._servers.append('Server 3')
        self._servers.append('Server 4')

    def change_server(self):
        self._servers.pop()
        self._servers.append('Server 5')


hc1 =HealthCheck()
hc2 =HealthCheck()

hc1.add_server()
for i in range(4):
    print(hc1._servers[i])

hc2.change_server()
for i in range(4):
    print(hc2._servers[i])

# 监控着服务器的动态 并及时更新
