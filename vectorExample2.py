# class of vector 2 and vector 3
import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x * other.x, self.y * other.y)
        if type(other) == int or type(other) == float:
            return Vec2(self.x - other, self.y - other)

    def magSq(self):
        # x^2 + y^2 = magnitude^2
        return self.x * self.x + self.y * self.y

    def mag(self):
        return math.sqrt(self.magSq())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angleBetween(self, other):
        # cos(theta) = (u dot v) / ([u] * [v])
        # theta = cos^-1((u dot v) / ([u] * [v])) 
        return math.acos(self.dot(other)/(int(self.mag())*int(other.mag())))

class Vec3():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vec3(self.x + other.x, self.y + other.y, self.z+ other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if type(other) == int or type(other) == float:
            return Vec3(self.x - other, self.y - other, self.z - other)

    def magSq(self):
        # x^2 + y^2 = magnitude^2
        return self.x * self.x + self.y * self.y + self.z * self.z

    def mag(self):
        return math.sqrt(self.magSq())

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angleBetween(self, other):
        # cos(theta) = (u dot v) / ([u] * [v])
        # theta = cos^-1((u dot v) / ([u] * [v])) 
        return math.acos(self.dot(other)/(self.mag*other.mag))



vec2 = Vec2(7,2)
multi = vec2.angleBetween(Vec2(4,3))
print(multi)
