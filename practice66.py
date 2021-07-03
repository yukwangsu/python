class Vector:
    def __init__(self, value):
        self.value = value
        a = 0
        for i in range(len(value)):
            a += value[i]**2
        self.amp = a**(1/2)
    def __add__(self, object):
        temp = [self.value[i] + object.value[i] for i in range(len(self.value))]
        return Vector(temp)
    def __mul__(self, object):
        s = 0
        for i in range(len(self.value)):
            s += self.value[i]*object.value[i] 
        return s    
    def __sub__(self, object):
        temp = [self.value[i] - object.value[i] for i in range(len(self.value))]
        return Vector(temp)