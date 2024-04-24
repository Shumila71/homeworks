class raises:
    def __init__(self,exc):
        self.exc = exc
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exc == exc_type:
            print(exc_type)
            return True
        else:
            print('True!')
            return True
with raises(ValueError):
    raise ValueError