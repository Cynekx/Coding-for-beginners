def przywitanie():  # tak sie 'programuje' funkcje, jesli takiej nie ma - to co jest
    print("Hej, Kinga")
def pozegnanie():
    print("Papatki!")
przywitanie()
print("musze leciec")
pozegnanie()

espanol = "hasta la vista"
def odpowiedz():
    print("Do zobaczenia, " + espanol)
odpowiedz()

''' a zeby dzialalo poza funkcją (nie tylko lokalnie trzeba zrobic return '''

def siema(kto):
    pozdrowienie = "Witaj," + kto #tworzenie nowej zmiennej
    return pozdrowienie  #zwraca zmienna pozdrowienie, kiedy w pozniejszym glownym kodzie bedzie wezwana
kto = "Kinga"  #definiujemy argument
pozdrowienie = siema(kto)
print(pozdrowienie)



''' proba'''
def chrupki(smak):
    chrupanie = "flips " + smak
    return chrupanie

smak = "czekoladowe" #trzeba zdefiniowac argument przed definiowaniejm funkcji
chrupanie = chrupki(smak)

print(chrupanie)


''' proba 3 '''

def kon(jaki):
    masci = "Cynia jest masci " + jaki
    return masci
jaki = "ciemnogniadej"
masci = kon(jaki)
print(masci)


''' proba 4 '''
def kot1(kolor1):
    Oliver = "Oliver mial siersc " + kolor1
    return Oliver
kolor1 = "bialo - czarna"
Oliver = kot1(kolor1)

def kot2(kolor2):
    Nela = "Nela ma masc " + kolor2
    return Nela
kolor2 = "szylkretowa"
Nela = kot2(kolor2)
print(Oliver)
print(Nela)
