def LargestSquare(n):
    m = 1
    while n >= m*m:
        m += 1
    q = (m-1)*(m-1)
    print("The largest square number before " + str(n) + " is " + str(q) + " which is the square of " + str(m-1))
    
LargestSquare(27)