class Macierz:

  def __init__(self, x):
    self.m = x

  def __str__(self):
    return str(self.m)

  def __add__(self, a):
    wynik = [[self.m[i][j] + a.m[i][j] for j in range(len(self.m))] for i in range(len(self.m[0]))]
    return wynik

  def __sub__(self, a):
    wynik = [[self.m[i][j] - a.m[i][j] for j in range(len(self.m))] for i in range(len(self.m[0]))]
    return wynik

  @staticmethod
  def odwrotna2x2(a):
    detA = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    if detA != 0:
      return [[a[1][1],-a[0][1]], [-a[1][0],a[0][0]]]

  @staticmethod
  def odwrotna3x3(x):
    return 0

macierz1 = Macierz([[3,5,-1],[4,0,2],[-7,1,6]])
macierz2 = Macierz([[2,3,8],[-9,11,-8],[-6,14,-9]])

print(macierz1 + macierz2)
print(macierz1 - macierz2)

print(Macierz.odwrotna2x2([[1,2],[3,4]]))
