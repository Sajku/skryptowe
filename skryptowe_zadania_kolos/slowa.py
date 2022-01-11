try:
  plik = open("TXT/tekst.txt", "r")
  plik2 = open("TXT/slowa.txt", "w")
except:
  print("Nie można wczytać pliku")
  exit()

plik2.write("słowo  | liczba wystąpień w systemie 10 | liczba wystąpień w systemie 2\n")
plik2.write("----------------------------------------------------------------------\n")

tekst = plik.read()
slowa = tekst.replace("\n", " ")
slowa = slowa.split(" ")
listaSlow = []

for x in slowa:
  if x not in listaSlow:
    listaSlow.append(x);

for x in listaSlow:
  wystapien = tekst.count(x)
  plik2.write(f"{x.ljust(6)} | {str(wystapien).rjust(10)} | {bin(wystapien).ljust(10)}\n")

spacje = tekst.count(" ")
entery = tekst.count("\n")

plik2.write(f"spacje | {str(spacje).rjust(10)} | {bin(spacje).ljust(10)}\n")
plik2.write(f"enter  | {str(entery).rjust(10)} | {bin(spacje).ljust(10)}\n")

