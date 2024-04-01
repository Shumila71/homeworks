class MyClass:
    def __init__(self):
        self.field1 = 1
        self._field2 = 2
        self.__field3 = 3

obj = MyClass()

for attr_name in dir(obj):
    if not attr_name.__contains__("__"):
        print(attr_name)