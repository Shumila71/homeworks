class MyClass:
    def method(self):
        print("я метод!")

obj = MyClass()
method_name = "method"

if hasattr(obj, method_name):
    method = getattr(obj, method_name)
    method()