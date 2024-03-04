def natural10():
    for i in range(1,11):
        print(i)
natural10()

def sum_of_numbers(n):
    suma_totala = sum(range(1, n+1))
    print("Suma totala a numerelor de la 1 la", n, "este:", suma_totala)
numar_dat = 5
sum_of_numbers(numar_dat)

def calc(a, b, c):
    total = a + b + c
    average = total / 3
    if average > 0:
        return average
rezultat = calc(10, 15, 20)
print(rezultat)