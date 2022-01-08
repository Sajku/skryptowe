def sprawdz(x):
  if "x" in x:
    dec1 = int(x, 16)
    oct1 = oct(int(x, 16))
    hex1 = x
  elif "o" in x:
    dec1 = int(x, 8)
    oct1 = x
    hex1 = hex(int(x, 8))
  else:
    dec1 = x
    oct1 = oct(int(x))
    hex1 = hex(int(x))

  return [str(dec1), str(oct1), str(hex1)]

try:
  plik1 = open("danezadanie2.txt", "r")
  liczby = plik1.read().splitlines()
except:
  print("BŁĄD! Nie można odczytać pliku")
  exit()

plik2 = open("wyjsciezad2.txt", "w")
plik2.write("L. dziesiętne | L. ósemkowe | L. szesnastkowe\n")
plik2.write("---------------------------------------------\n")

for liczba in liczby:
  try:
    wynik = sprawdz(liczba)
    plik2.write(f"{wynik[0].ljust(14,'-')}|{wynik[1].center(13,'-')}|{wynik[2].rjust(16,'-')}\n")
  except:
    print("Zła wartość!")
