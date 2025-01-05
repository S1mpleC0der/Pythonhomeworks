def find_edges(num1, num2, num3):
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    print(f'{maximum} is largest and {minimum} is smallest')

find_edges(3, 1, 2)