from classes import Matrix2

def nthFib(n):
    if n == 0:
        return 0
    
    base = Matrix2(1, 1, 1, 0)
    return (base ** n).elements[0][1]

for i in range(10):
    print(nthFib(i))