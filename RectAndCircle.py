import math

class Rectangle:
    def __init__(self, x0, y0, height, width):
        self.x0 = x0
        self.y0 = y0
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def intersection_area(self, other):
        x_overlap = max(0, min(self.x0 + self.width / 2, other.x0 + other.width / 2) - max(self.x0 - self.width / 2, other.x0 - other.width / 2))
        y_overlap = max(0, min(self.y0 + self.height / 2, other.y0 + other.height / 2) - max(self.y0 - self.height / 2, other.y0 - other.height / 2))
        return x_overlap * y_overlap


class Circle:
    def __init__(self, x0, y0, r):
        self.x0 = x0
        self.y0 = y0
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)

    def perimeter(self):
        return 2 * math.pi * self.r

    def intersection_area(self, other):
        d = math.sqrt((self.x0 - other.x0) ** 2 + (self.y0 - other.y0) ** 2)
        r1 = self.r
        r2 = other.r

        # Если круги не пересекаются
        if d >= r1 + r2:
            return 0

        # Если одна окружность полностью находится внутри другой
        if d <= abs(r1 - r2):
            return math.pi * min(r1, r2) ** 2

        r1_sq = r1 ** 2
        r2_sq = r2 ** 2

        a = r1_sq * math.acos((d ** 2 + r1_sq - r2_sq) / (2 * d * r1))
        b = r2_sq * math.acos((d ** 2 + r2_sq - r1_sq) / (2 * d * r2))
        c = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))

        return a + b - c