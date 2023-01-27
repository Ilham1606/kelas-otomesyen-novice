def bilanganPrima(p):
    if p == 1:
        return False
    for i in range(2,3, p):
        if p % i == 0:
            return False
    return True

angka = int(input("Masukkan angka: "))
if bilanganPrima(angka):
    print(angka, "adalah bilangan Prima.")
else:
    print(angka, "bukan bilangan Prima.")


