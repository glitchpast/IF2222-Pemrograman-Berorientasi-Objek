"""
Abstract Class adalah sebuah kelas yang berfungsi sebagai template untuk kelas lain.
Kelas ini tidak dapat diinstansiasi. Metode dalam kelas abstrak harus diimplementasikan oleh kelas yang mewarisi kelas abstrak tersebut. Jika tidak diimplementasikan, maka akan terjadi error.
Interface adalah sebuah kontrak yang mendefinisikan metode yang harus diimplementasikan oleh kelas yang mewarisi interface tersebut. Kelas ini juga tidak dapat diinstansiasi

Perbedaan utama antara abstract class dan interface adalah:
1. Abstract class dapat memiliki implementasi metode, sedangkan interface tidak dapat memiliki implementasi metode.
2. Abstract class dapat memiliki atribut, sedangkan interface tidak dapat memiliki atribut.
3. Abstract class dapat memiliki konstruktor, sedangkan interface tidak dapat memiliki konstruktor.
"""

from abc import ABC, abstractmethod

class BangunDatar(ABC):
  @abstractmethod
  def luas(self):
    pass

  @abstractmethod
  def keliling(self):
    pass

class ShowDetails(ABC):
  @abstractmethod
  def menampilkan_detail(self):
    pass

class Persegi(BangunDatar, ShowDetails):
  def __init__(self, sisi):
    self.sisi = sisi

  def luas(self):
    return self.sisi * self.sisi

  def keliling(self):
    return 4 * self.sisi

  def menampilkan_detail(self):
    return f"Persegi dengan sisi {self.sisi}, luas {self.luas()}, keliling {self.keliling()}"

class Lingkaran(BangunDatar, ShowDetails):
  def __init__(self, radius):
    self.radius = radius

  def luas(self):
    return 3.14 * self.radius * self.radius

  def keliling(self):
    return 2 * 3.14 * self.radius

  def menampilkan_detail(self):
    return f"Lingkaran dengan radius {self.radius}, luas {self.luas()}, keliling {self.keliling()}"

def main():
  persegi = Persegi(4)
  lingkaran = Lingkaran(3)

  print(persegi.menampilkan_detail())
  print(lingkaran.menampilkan_detail())

if __name__ == "__main__":
  main()
