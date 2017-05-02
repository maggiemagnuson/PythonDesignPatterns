# import the Abstract Base Class
import MyABC

class MyClass(MyABC.MyABC):
    def __init__(self, value=1):
        self._myprop = value

    def do_something(self, value):
        print(value)
        print(self._myprop)
        self._myprop *= 2 + value

    @property
    def some_property(self):
        return self._myprop


print("--> starting main()")
mc = MyClass()
mc.do_something(4)
print (mc.some_property)