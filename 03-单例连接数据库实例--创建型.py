import sqlite3


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):    # ptython 可以通过特殊的call方法可以通过元类创建单例
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        cursor_obj = None
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            cursor_obj = self.connection.cursor()
        return cursor_obj


"""
只能创建一个实例  共用同一个数据库时就会使用到   但是会出现集体群开发的时候 没创建一个web实例就要创建一个单例  造成数据库资源竞争/不能同步等问题  变用到数据库连接池
"""
db1 = Database().connect()
db2 = Database().connect()

print(db1)
print(db2)
