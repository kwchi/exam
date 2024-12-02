a = 1
b = 1
n = int(input("Кількість: "))

def progression(a, b, n):

    sum_n = ((a + (a + b * n)) / 2) * n
    return  sum_n

print(progression(a, b, n))