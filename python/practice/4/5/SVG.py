class SVG(object):


    def __init__(self):
        self.svg_list = []
        self.width = 0
        self.height = 0

        self.templates = self.__generate_templates()

    def __add_to_svg(self, text):
        self.svg_list.append(str(text))

    def __generate_templates(self):
        templates = {}

        templates["create"] = "<svg width='{}px' height='{}px' xmlns='http://www.w3.org/2000/svg' version='1.1'>\n"
        templates["finalize"] = "</svg>"
        templates["circle"] = "    <circle fill='{}' r='{}' cy='{}' cx='{}' />\n"
        templates["line"] = "    <line stroke='{}' y2='{}' x2='{}' y1='{}' x1='{}' />\n"
        templates["rectangle"] = "    <rect fill='{}' stroke='{}' stroke-width='{}px' width='{}' height='{}' y='{}' x='{}' ry='{}' rx='{}' />\n"
        templates["text"] = "    <text x='{}' y = '{}' font-family='{}' stroke='{}' fill='{}' font-size='{}px'>{}</text>\n"
        templates["ellipse"] = "   <ellipse cx='{}' cy='{}' rx='{}' ry='{}' fill='{}' stroke='{}' stroke-width='{}' />\n"

        return templates

    def circle(self, cx, cy,r=4,color='black'):
        self.__add_to_svg(self.templates["circle"].format( color, r, cy, cx))

    def line(self, x1, y1, x2, y2, color='black'):
        self.__add_to_svg(self.templates["line"].format(color, y2, x2, y1, x1))

    def rectangle(self, width, height, x, y, fill, stroke, strokewidth, radiusx, radiusy):
        self.__add_to_svg(self.templates["rectangle"].format(fill, stroke, strokewidth, width, height, y, x, radiusy, radiusx))

    def fill(self, Fill):
        self.rectangle(self.width, self.height, 0, 0, Fill, Fill, 0, 0, 0)

    def text(self, x, y, fontfamily, fontsize, fill, stroke, text):
        self.__add_to_svg(self.templates["text"].format(x, y, fontfamily, stroke, fill, fontsize, text))

    def ellipse(self, cx, cy, rx, ry, fill, stroke, strokewidth):
        self.__add_to_svg(self.templates["ellipse"].format(cx, cy, rx, ry, fill, stroke, strokewidth))

    def __str__(self):
        return("".join(self.svg_list))

    def save(self, path,wid,heigh):

        f = open(path, "w+")
        f.write(self.templates["create"].format(wid,heigh))
        f.write(str(self))
        f.write('</svg>')
        f.close()