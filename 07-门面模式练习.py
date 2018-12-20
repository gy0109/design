# 厨师做菜-- 荤配 素配 酒配 洗碗   -----由老板决定给厨师


class ChefManager(object):
    def __init__(self):
        pass

    def make_vegetables(self):
        MeatVegetables().cook_meat()   # 荤菜师父做荤菜
        DishesVegetables().cook_dishes()   # 素菜师父做素菜
        CockTail().cook_tail()   # 调酒师父做调酒
        WashDishes().wash()   # 洗碗阿姨去洗碗


class MeatVegetables(object):
    def __init__(self):
        print('meat_vegetables   荤菜')

    def cook_meat(self):
        print('荤菜')


class DishesVegetables(object):
    def __init__(self):
        print('素菜 dishes_vegetables')

    def cook_dishes(self):
        print('cook_dishes')


class CockTail(object):
    def __init__(self):
        print('Cocktail 调酒')

    def cook_tail(self):
        print('cook_tail')


class WashDishes(object):
    def __init__(self):
        print('WashDishes')

    def wash(self):
        print('wash_dishes')


class Boos(object):
    def __init__(self):
        print('It is boss')

    def greeting_guest(self):
        print('客人点完菜')
        ChefManager().make_vegetables()

    def __del__(self):
        print('工作完成')

Boos().greeting_guest()
