class Sortowanie:
  def babelkowe(a):
    for i in range(len(a)):
      for j in range(len(a) - 1):
        if a[j] > a[j+1]:
          a[j], a[j+1] = a[j+1], a[j]
    return a

  def shella(array):
    part = len(array) // 2
    gap = part
    while part > 0:
      for i in range(part, gap):
        temp = array[i]
        j = i
        while j >= part and array[j - part] > temp:
          array[j] = array[j - part]
          j -= part

        array[j] = temp
      part //= 2
    return array


try:
  plik = open("TXT/sortowanie.txt", "r")
except:
  print("Nie można otworzyć pliku")
  exit()

try:
  listy = plik.read().splitlines()
  listy = [[int(x) for x in linia.split(" ")] for linia in listy]
except:
  print("Złe dane!")
  exit()

plik2 = open("TXT/sortowanie-wynik.txt", "w")

for i in listy:
  posortowaneB = Sortowanie.babelkowe(i)
  posortowaneS = Sortowanie.shella(i)
  plik2.write(str(posortowaneB) + "\n")
  plik2.write(str(posortowaneS) + "\n")

