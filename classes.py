class Vector2:
    def __init__(self, a:float, b:float):
        # [0, 1]
        # x, y
        self.elements = [a, b]
    
    def __mult__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(other * self.elements[0], other * self.elements[1])
        
    def __rmult__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(other * self.elements[0], other * self.elements[1])

    def __str__(self):
        return f"{[self.elements[0], self.elements[1]]}"

class Matrix2:
    def __init__(self, a:float, b:float, c:float, d:float):
        if abs(round(a) - a) < 0.0000001:
            a = round(a)
        if abs(round(b) - b) < 0.0000001:
            b = round(b)
        if abs(round(c) - c) < 0.0000001:
            c = round(c)
        if abs(round(d) - d) < 0.0000001:
            d = round(d)
        # [0,0, 0,1]
        # [1,0, 1,1]
        # Row,Column
        self.elements = [
                            [a, b],
                            [c, d]
                        ]
        
    def __mul__(self, other):
        if type(other) == Matrix2:
            return Matrix2(self.elements[0][0] * other.elements[0][0] + self.elements[0][1] * other.elements[1][0],
                           self.elements[0][0] * other.elements[0][1] + self.elements[0][1] * other.elements[1][1],
                           self.elements[1][0] * other.elements[0][0] + self.elements[1][1] * other.elements[1][0],
                           self.elements[1][0] * other.elements[0][1] + self.elements[1][1] * other.elements[1][1]
                           )
        elif type(other) == Vector2:
            return Vector2(self.elements[0][0] * other.elements[0] + self.elements[0][1] * other.elements[1],
                           self.elements[1][0] * other.elements[0] + self.elements[1][1] * other.elements[1]
                           )
        elif type(other) == int or type(other) == float:
            return Matrix2(other * self.elements[0][0],
                           other * self.elements[0][1],
                           other * self.elements[1][0],
                           other * self.elements[1][1]
                           )
    
    def __rmul__(self, other):
        if type(other) == Matrix2:
            return Matrix2(other.elements[0][0] * self.elements[0][0] + other.elements[0][1] * self.elements[1][0],
                           other.elements[0][0] * self.elements[0][1] + other.elements[0][1] * self.elements[1][1],
                           other.elements[1][0] * self.elements[0][0] + other.elements[1][1] * self.elements[1][0],
                           other.elements[1][0] * self.elements[0][1] + other.elements[1][1] * self.elements[1][1]
                           )
        elif type(other) == int or type(other) == float:
            return Matrix2(other * self.elements[0][0],
                           other * self.elements[0][1],
                           other * self.elements[1][0],
                           other * self.elements[1][1]
                           )
    
    def __add__(self, other):
        if type(other) == Matrix2:
            return Matrix2(
                self.elements[0][0] + other.elements[0][0],
                self.elements[0][1] + other.elements[0][1],
                self.elements[1][0] + other.elements[1][0],
                self.elements[1][1] + other.elements[1][1]
            )
        else:
            raise("Only add same dimension matrices together")

    def determinant(self):
        return self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]
    
    def inverse(self):
        return 1/self.determinant() * Matrix2(self.elements[1][1], 
                                              -self.elements[0][1],
                                              -self.elements[1][0],
                                              self.elements[0][0]
                                              )

    def __pow__(self, other:int):
        if other == -1:
            return self.inverse()
        elif other <= 0:
            raise("Only raise to positive integer powers")
        elif other == 1:
            return self
        else:
            result = Matrix2(1,0,0,1)
            base = self
            while other > 0:
                if other % 2 == 1:
                    result *= base
                base *= base
                other //= 2    
                
            return result

    def __str__(self):
        return f"{[self.elements[0][0], self.elements[0][1], self.elements[1][0], self.elements[1][1]]}"

if __name__ == "__main__":
    matrix1 = Matrix2(1,5,2,6)
    matrix2 = Matrix2(1,2,7,4)
    vector = Vector2(1, 6)

    print((matrix1 ** 1))