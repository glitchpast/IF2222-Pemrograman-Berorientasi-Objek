class Motor:
  def __init__(self, warna, merk, tahun):
    self.warna = warna
    self.merk = merk
    self.tahun = tahun
  
  def tampilkan_info(self):
    print(f"Motor {self.merk} berwarna {self.warna} tahun {self.tahun}")


def main():
  motor1 = Motor("Merah", "Yamaha", 2020)
  motor2 = Motor("Biru", "Honda", 2021)

  motor1.tampilkan_info()
  motor2.tampilkan_info()

if __name__ == "__main__":
  main()
