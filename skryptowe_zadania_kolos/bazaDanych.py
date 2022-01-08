def analizuj(dane):
  for wiersz in dane:
    x = wiersz.split(";")
    plik2.write(f"{x[0].ljust(15)} | ")
    rokU = x[1].split(".")[2]
    rokZ = x[4].split(".")[2]
    lata = str(int(rokZ)-int(rokU)) + " lat"
    plik2.write(f"{lata.center(9)} | ")
    if x[2] == x[5]:
      miasto = "Tak"
    else:
      miasto = "Nie"
    plik2.write(f"{miasto.center(9)} | ")

    if x[3] == x[6]:
      kraj = "Tak"
    else:
      kraj = "Nie"
    plik2.write(f"{kraj.center(9)}\n")

try:
  plik1 = open("TXT/baza.txt", "r", encoding="utf8")
  plik2 = open("TXT/analizadanych.txt", "w")
except:
  print("BŁĄD! Nie można otworzyć pliku")
  exit()

dane = plik1.read().splitlines()
plik2.write("osoba | żył lat | ur. i zm. w tym samym mieście | ur. i zm. w tym samym kraju\n")
plik2.write("-----------------------------------------------------------------------------\n")
analizuj(dane)
