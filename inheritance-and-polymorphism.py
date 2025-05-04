'''
Inheritance adalah fitur dalam pemrograman berorientasi objek yang memungkinkan sebuah kelas untuk mewarisi atribut dan metode dari kelas lain. Ini memungkinkan kita untuk membuat hierarki kelas yang lebih terstruktur dan mengurangi duplikasi kode.
Polymorphism adalah kemampuan untuk menggunakan objek dari kelas yang berbeda dengan cara yang sama. Dalam Python, kita dapat mencapai polymorphism dengan menggunakan metode yang memiliki nama yang sama tetapi diimplementasikan dengan cara yang berbeda dalam kelas yang berbeda.
'''

class Laptop:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def display_info(self):
    print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

class GamingLaptop(Laptop):
  def __init__(self, brand, model, price, gpu):
    super().__init__(brand, model, price)
    self.gpu = gpu

  def display_info(self):
    print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, GPU: {self.gpu}")

class BusinessLaptop(Laptop):
  def __init__(self, brand, model, price, battery_life):
    super().__init__(brand, model, price)
    self.battery_life = battery_life

  def display_info(self):
    print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Battery Life: {self.battery_life}")

def main():
  gaming_laptop = GamingLaptop("Alienware", "M15", 2000, "NVIDIA RTX 3080")
  business_laptop = BusinessLaptop("Dell", "XPS 13", 1500, "12 hours")

  gaming_laptop.display_info()
  business_laptop.display_info()

if __name__ == "__main__":
  main()
