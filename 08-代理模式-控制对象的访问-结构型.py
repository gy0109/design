"""
代理模式的特点:   寻求方和提供方之间的代理服务器,将寻求方的请求进行评估,然后发给响应的提供方,并将提供方提供的数据返回给寻求方
代理充当实际对象接口类,对象可以使多种类型的,实际上就是封装实际服务对象的包装器和代理人,可以为其包装的对象提供服务,并且无需改动代码,
主要目的: 为其他对象提供一个代理者或者占位符,从而控制实际对象的访问

使用场景:
1,以简单的方式表示一个复杂的系统 -- 复杂计算的系统
2,提高现有的实际对象的安全性 -- 恶意活动
3,不同服务器上的远程对象提供本地接口 -- 远程连接服务器
4,消耗大量内存的对象提供一个轻量级的句柄
"""

"""
代理模式: 
1, 虚拟代理:如果一个对象实例化需要大量的内存,便先利用占位符来表示 (大量图片-不加载-提示有图-点击显示--省去加载大型图片的开销)
2, 远程代理:远程服务器或者不同地址的实际对象提供实际本地 (监控系统获取多个服务器的cpu和内存,监控实时运行的上下文--执行远程命令一获取参数值)
3, 保护代理:控制对真实主题的控制访问 认证服务充当负责认证和授权的保护性代理服务器 有助域保护网站的核心功能 防止无法识别或未授权的代理访问 检查调用者是否具有转发请求所需的访问权限
4, 智能代理:在访问时添加其他操作   资源共享锁  智能的检测核心组件是否被锁,确保其他对象没有修改他
"""
from abc import ABCMeta, abstractmethod


# 不接触底层组件 便可以访问和控制 -- 代理 支持分布式访问
class Actor(object):
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__)

    def available(self):
        self.is_busy = False
        print(type(self).__name__)

    def get_status(self):
        return self.is_busy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        actor = Actor()
        if actor.get_status():
            actor.occupied()
        else:
            actor.available()


# 现实中刷卡的案例
class You(object):
    def __init__(self):
        print('假如你要买一件衬衫')
        self.debit_card = DebitCard()
        self.is_purchased = None          # 购买

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print('买好了')
        else:
            print('钱不够')


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def _get_account(self):
        return self.card

    def _has_funds(self):
        print('您的账户是:', self._get_account())
        return True

    def set_card(self, card_num):
        self.card = card_num

    def do_pay(self):
        if self._has_funds():
            print('购买成功!')
            return True
        else:
            print('购买失败')
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        self.bank.set_card(input('请输入卡号:'))
        return self.bank.do_pay()


if __name__ == '__main__':
    # Agent().work()
    You().make_payment()
