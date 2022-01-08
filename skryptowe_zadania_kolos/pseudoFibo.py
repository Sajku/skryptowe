class PseudoFibo:

  def __init__(self, tab, j, k, m):
    self.tab = tab
    self.j = j
    self.k = k
    self.m = m

  def __add__(self, j, k):
    return self.tab[self.j - 1] + self.tab[self.k - 1] % self.m

  def __sub__(self, j, k):
    return self.tab[self.j - 1] - self.tab[self.k - 1] % self.m

  def __truediv__(self, j, k):
    return self.tab[self.j - 1] // self.tab[self.k - 1] % self.m


pf1 = PseudoFibo([1,2,3,4,5,6,7,8,9,10],1,3,10)
