# python implementation of vectors with operation functions
import math


class Vector():
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def add(self, vector1):
        added = Vector(self.x + vector1.x , self.y + vector1.y , self.z + vector1.z)
        return added

    def sub(self, vector1):
        subbed = Vector(self.x - vector1.x , self.y - vector1.y , self.z - vector1.z)
        return subbed

    def dot(self, vector1):
        dotted = self.x * vector1.x + self.y * vector1.y + self.z * vector1.z
        return dotted

    def multi(self, scalar):
        multied = Vector(self.x * scalar , self.y * scalar , self.z * scalar)
        return multied

    def lengthsq(self, vector):
        # pythagoras - make a right angled triangle from angle.
        # y value is height of triangle
        # x value is width of triangle
        # therefore: x^2 + y^2 = length^2
        length = vector.x^2+vector.y^2
        return length

    def angle(self, vector1):
        # find lenths of each vector
        length = Vector.lengthsq(self)
        length1 = Vector.lengthsq(vector1)
        # formula for finding angle between two vectors is:
        # CosӨ = U*V/lengthU*lengthV
        # therefore: Ө = Cos^-1(U*V/lengthU*lengthV)
        midangle = math.acos(Vector.dot(vector1)/length*length1)
        return midangle

