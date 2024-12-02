a = 1
b = 1
n = int(input("Кількість: "))

class Pr:
    @staticmethod
    def progression(a, b, n):
        sum_n = ((a + (b * n)) / 2) * n
        return  sum_n

pr = Pr()
summ = pr.progression(a, b, n)
print(summ)