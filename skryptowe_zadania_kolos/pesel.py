class Pesel:
  def __init__(self, pesel):
    self.iloscDni = [31,28,31,30,31,30,31,31,30,31,30,31]
    self.poprawny = 1
    self.pesel = pesel
    self.rok = pesel[0:2]
    self.miesiac = pesel[2:4]
    self.dzien = pesel[4:6]
    self.plec = pesel[6:10]
    self.sm = int(pesel[10:11])

  def poprawnosc(self):
    wagi = [1,3,7,9,1,3,7,9,1,3]
    ostatnia = 0
    for i in range(len(wagi)):
      ostatnia += wagi[i] * int(self.pesel[i])
    ostatnia = (10 - (ostatnia % 10)) % 10

    if ostatnia != self.sm:
      self.poprawny = 0

    if int(self.miesiac) >= 13:
      self.miesiac = int(self.miesiac) % 20
    if int(self.dzien) >= self.iloscDni[int(self.miesiac)-1]:
      self.poprawny = 0

    if self.poprawny:
      print("Pesel poprawny!")
    else:
      print("Pesel nie jet poprawny!")

pesel1 = Pesel("81010200141")
pesel1.poprawnosc()
