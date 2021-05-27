import math

class Triangulo:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro (self):
        perimetro = self.a+self.b+self.c
        return perimetro
    
    def tipo_lado(self):
        if (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b)or (self.b == self.c and self.a !=self.b):
            return ('isósceles')
        elif self.a == self.b == self.c:
            return ('equilátero')
        else:
            return ('escaleno')

    def retangulo(self):
        a , b, c = self.a, self. b, self.c
        if c == math.hypot (b,a) or  b == math.hypot (a,c) or a == math.hypot (b,c):
            return True
        else:
            return False
