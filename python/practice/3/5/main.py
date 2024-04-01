def load_config(filename):
    with open(filename, 'r') as file:
        config_script = file.read()
    config_globals = {}
    exec(config_script, config_globals)
    return config_globals

config = load_config('D:\\code\\_4\\python\\practice\\3\\5\\config.py')

print("Host:", config)