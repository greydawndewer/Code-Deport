def squares(x):
    square = x**2
    res1 = square - x
    res2 = square - x*x/x
    print(res1)
    print(res2)
    if res1 == res2:

        print("1")
    else:
        print("0")
squares(908986)


