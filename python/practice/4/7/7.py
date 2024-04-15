import inspect

file = "module.py"
module = inspect.getmodulename(file)
x = ""
moduke = __import__(module)
for i in moduke.__dir__()[8:]:
    obj = moduke.__getattribute__(i)
    if inspect.isclass(obj):
        print(f"## Класс {i}")
    if inspect.isfunction(obj):
        print(f"## Функция {i}{inspect.signature(obj)}")
    for j in obj.__doc__.split("\n"):
        print(j.lstrip())
    if inspect.isclass(obj):
        for key, values in obj.__dict__.items():
            if inspect.isfunction(values):
                print(f"* **Метод** `{key}{inspect.signature(values)}`")
                for j in values.__doc__.split("\n"):
                    print(j.lstrip())
