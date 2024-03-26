class Tag:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __enter__(self):
        print(f'<{self.name}>')
        return self

    def __exit__(self, type, value, traceback):
        print(f'</{self.name}>')

class HTML:
    def __init__(self):
        self.root = Tag('html')

    def get_code(self):
        for child in self.root.children:
            print(child)

    def body(self):
        return Tag('body')

    def div(self):
        return Tag('div')

    def p(self, text):
        print(f'    <p>{text}</p>')


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

html.get_code()