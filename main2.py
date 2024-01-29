produkty = {
    "klawiatura": 200,
    "cpu": 300,
    "gpu": 500,
    "ram": 200,
    "obudowa": 100
}
koszyk = {}


print("Witaj w Z-COM")
print("Nasze produkty to: ")
for produkt, cena in produkty.items():
    print(produkt, ": " + str(cena), " zł")
new_product = ""

while new_product != "koniec":
    new_product = input("Podaj produkt jaki dodac do koszyka: ")
    print("Jeśli chcesz zakończyć wpisz: koniec ")

    if new_product in produkty:
        koszyk[new_product] = produkty[new_product]
        print("Dodano do koszyka: ", new_product)
    elif new_product == "koniec":
        print("Koniec zakupu")
        imie = input("Podaj imie: ")
    else:
        decyzja = input("Nie ma takiego produktu w bazie, Czy chcesz dodać taki produkt? (Tak/Nie): ")
        while decyzja != "nie":
            nowa_cena = int(input("Podaj cene tego produktu"))
            produkty[new_product] = nowa_cena
            break


print("Twój koszyk:")
suma = 0
for produkt, cena in koszyk.items():
    print(f"{produkt}: {cena} zł")
    suma += cena
print("Suma od zapłaty", suma, " zł")
print("Dziękujemy za zakupy w Z-COM, Pan/Pani", imie)

