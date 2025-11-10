from classes import Matrix2

def nthFib(n):
    if n == 0:
        return 0
    
    if n > 0:
        base = Matrix2(1, 1, 1, 0)
    else:
        n = -n
        base = Matrix2(0, 1, 1, -1)
    return (base ** n).elements[0][1]

if __name__ == "__main__":
    print(nthFib(-10000))