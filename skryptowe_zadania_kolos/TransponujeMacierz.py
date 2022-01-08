def transponowanie(x):
  wynik = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
  return wynik

try:
  plik1 = open("TXT/macierzwejsciowa.txt", "r")
  plik2 = open("TXT/macierzwynikowa.txt", "w")
except:
  print("BŁĄD z plikiem!")
  exit()

macierz = []
try :
  macierz = plik1.read().splitlines()
  macierz = [[int(x) for x in linia.split(" ")] for linia in macierz]
except:
  print("BŁĄD! Podano niewłaściwą macierz")
  exit()

print(macierz)
macierz2 = transponowanie(macierz)
print(macierz2)

for a in macierz2:
  plik2.write(f"{a}\n")
