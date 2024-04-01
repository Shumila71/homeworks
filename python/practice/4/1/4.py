get_inheritance = lambda cls: ' --> '.join([cls.__name__] + get_inheritance(cls.__base__).split(' --> ') if cls.__base__ else [cls.__name__])
print(get_inheritance(OSError))