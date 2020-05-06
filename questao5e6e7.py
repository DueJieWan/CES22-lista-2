class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_x(self):
        return [self.x, -1*self.y]

    def slope_from_origin(self):
        if self.y:
            return self.y/self.x
        else:
            return "NaN"

    def get_line_to(self, dot2):
        m = (self.y-dot2.y)/(self.x-dot2.x)
        return (m, self.y-m*self.x )

dot = Point(3, 5)
print(dot.reflect_x())
print(Point(4, 10).slope_from_origin())
print(Point(4, 11).get_line_to(Point(6, 15)))