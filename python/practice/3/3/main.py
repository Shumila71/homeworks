'''
Изменение значения глобальной переменной GLOBAL_VAR в модуле не приведет к тому, 
что это новое значение отразится на всех пользователях этого модуля. 
Каждый пользователь импортирует переменную GLOBAL_VAR как отдельный объект, и изменение значения этого 
объекта не повлияет на других пользователей модуля.
'''
from some_module import GLOBAL_VAR
GLOBAL_VAR = 42

'''
Вместо этого, если вы хотите, чтобы изменения переменной отразились на всех пользователях модуля, 
можно использовать класс с атрибутом класса вместо глобальной переменной. Например:
class GlobalVar:
    value = 42
'''