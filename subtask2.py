def CountSumMinMean():
    n = 0
    x = []
    while True:
        user_num = int(input("Enter a natural number (or -1 to stop): "))
        if user_num == -1:
            break
        else:
            n += 1
            x.append(user_num)
        if n == 0:
            s = 0
            m = -1
            a = -1
        else:
            s = sum(x)
            m = min(x)
            a = s/n
    print("For your sequence " + str(x) + ", the count is " + str(n) + ", the sum is " + str(s) + ", the minimum is " + str(m) + " and the mean is " + str(a))

CountSumMinMean()