import xml.etree.ElementTree as ET

class SVG:
    def __init__(self):
        self.elements = []

    def line(self, x1, y1, x2, y2, color='black'):
        line_attrib = {
            'x1': str(x1),
            'y1': str(y1),
            'x2': str(x2),
            'y2': str(y2),
            'stroke': color
        }
        self.elements.append(('line', line_attrib))

    def circle(self, cx, cy, r, color='black'):
        circle_attrib = {
            'cx': str(cx),
            'cy': str(cy),
            'r': str(r),
            'fill': color
        }
        self.elements.append(('circle', circle_attrib))

    def save(self, filename, width, height):
        svg_attrib = {
            'version': '1.1',
            'width': str(width),
            'height': str(height),
            'xmlns': 'http://www.w3.org/2000/svg'
        }
        svg = ET.Element('svg', svg_attrib)
        
        for elem_type, elem_attrib in self.elements:
            ET.SubElement(svg, elem_type, elem_attrib)

        tree = ET.ElementTree(svg)
        tree.write(filename)

# Пример использования
svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)
