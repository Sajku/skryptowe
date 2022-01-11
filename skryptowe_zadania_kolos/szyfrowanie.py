class Szyfrowanie:
  def __init__(self, x):
    self.a = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    try:
      self.plik = open(x, "r")
      self.tresc = self.plik.read().splitlines()
      self.plik.close()
      self.nazwaPliku = x
    except:
      print("BŁĄD!")
      exit()

  def szyfruj(self):
    plik = open(self.nazwaPliku, "w")
    for linia in self.tresc:
      kod = ""
      for litera in linia:
        if litera in self.a:
          kod += self.a[(self.a.find(litera) + 1) % len(self.a)]
      plik.write(f"{kod}\n")
    plik.close()

  def deszyfruj(self):
    plik = open(self.nazwaPliku, "w")
    for linia in self.tresc:
      tekst = ""
      for litera in linia:
        if litera in self.a:
          tekst += self.a[(self.a.find(litera) - 1) % len(self.a)]
      plik.write(f"{tekst}\n")
    plik.close()


szyfr1 = Szyfrowanie("TXT/szyfr1.txt")
szyfr2 = Szyfrowanie("TXT/szyfr2.txt")

szyfr1.szyfruj()
szyfr2.deszyfruj()
