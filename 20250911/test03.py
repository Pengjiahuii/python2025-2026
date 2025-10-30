def average(*args):

    total = 0
    for num in args:
        total += num
    return total / len(args)

print(average(1, 2, 3, 4, 5))

