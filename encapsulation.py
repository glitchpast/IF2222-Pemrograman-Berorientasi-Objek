"""
Encapsulation adalah salah satu prinsip dasar dalam pemrograman berorientasi objek (OOP) yang menyembunyikan detail implementasi dari suatu objek dan hanya memperlihatkan antarmuka yang diperlukan untuk berinteraksi dengan objek tersebut.
Dalam Python, kita dapat menggunakan atribut privat (dengan menambahkan dua garis bawah di depan nama atribut) untuk mencapai encapsulation. Kemudian kita dapat menggunakan metode getter dan setter untuk mengakses dan memodifikasi atribut tersebut.
"""

class Lagu:
  def __init__(self, penyanyi, judul, tahun):
    self.__penyanyi = penyanyi
    self.__judul = judul
    self.__tahun = tahun

  def get_penyanyi(self):
    return self.__penyanyi
  
  def get_judul(self):
    return self.__judul
  
  def get_tahun(self):
    return self.__tahun
  
  def set_penyanyi(self, penyanyi):
    self.__penyanyi = penyanyi

  def set_judul(self, judul):
    self.__judul = judul

  def set_tahun(self, tahun):
    self.__tahun = tahun

class Playlist:
  def __init__(self):
    self.__daftar_lagu = []
    self.__lagu_yang_dimainkan_saat_ini = None

  def mencetak_lagu(self, prefix):
    if self.__lagu_yang_dimainkan_saat_ini is not None:
      lagu = self.__daftar_lagu[self.__lagu_yang_dimainkan_saat_ini]
      print(f"{prefix}: {lagu.get_judul()} oleh {lagu.get_penyanyi()}")
    else:
      print("Tidak ada lagu yang sedang dimainkan.")

  def putar_lagu_pertama(self):
    if self.__daftar_lagu:
      self.__lagu_yang_dimainkan_saat_ini = 0
      self.mencetak_lagu("Memutar lagu pertama")
    else:
      print("Tidak ada lagu dalam playlist.")
  
  def putar_lagu_terakhir(self):
    if self.__daftar_lagu:
      self.__lagu_yang_dimainkan_saat_ini = len(self.__daftar_lagu) - 1
      self.mencetak_lagu("Memutar lagu terakhir")
    else:
      print("Tidak ada lagu dalam playlist.")

  def putar(self):
    self.mencetak_lagu("Memutar")
  
  def putar_lagu_sebelumnya(self):
    if self.__lagu_yang_dimainkan_saat_ini is not None and self.__lagu_yang_dimainkan_saat_ini > 0:
      self.__lagu_yang_dimainkan_saat_ini -= 1
      self.mencetak_lagu("Memutar lagu sebelumnya")
    else:
      print("Tidak ada lagu sebelumnya.")

  def putar_lagu_selanjutnya(self):
    if self.__lagu_yang_dimainkan_saat_ini is not None and self.__lagu_yang_dimainkan_saat_ini < len(self.__daftar_lagu) - 1:
      self.__lagu_yang_dimainkan_saat_ini += 1
      self.mencetak_lagu("Memutar lagu selanjutnya")
    else:
      print("Tidak ada lagu selanjutnya.")

  def set_lagu(self, index):
    if 0 <= index < len(self.__daftar_lagu):
      self.__lagu_yang_dimainkan_saat_ini = index
      self.mencetak_lagu("Memutar lagu")
    else:
      print("Index lagu tidak valid.")

  def tambah_lagu(self, lagu):
    if isinstance(lagu, Lagu):
      self.__daftar_lagu.append(lagu)
      print(f"Lagu '{lagu.get_judul()}' oleh {lagu.get_penyanyi()} ditambahkan ke playlist.")
    else:
      print("Objek bukan merupakan lagu yang valid.")

def main():
  lagu1 = Lagu("Penyanyi 1", "Judul 1", 2020)
  lagu2 = Lagu("Penyanyi 2", "Judul 2", 2021)
  lagu3 = Lagu("Penyanyi 3", "Judul 3", 2022)

  playlist = Playlist()
  playlist.tambah_lagu(lagu1)
  playlist.tambah_lagu(lagu2)
  playlist.tambah_lagu(lagu3)

  playlist.putar_lagu_pertama()
  playlist.putar_lagu_terakhir()
  playlist.putar()
  playlist.putar_lagu_sebelumnya()
  playlist.putar_lagu_selanjutnya()
  playlist.set_lagu(1)

if __name__ == "__main__":
  main()
