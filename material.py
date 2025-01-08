from turtle import Turtle
import random

# Kelas induk Material
class Material():
    def __init__(self, shape, color, size, speed):
        self.objects = []  # Daftar objek yang dibuat
        self.shape = shape
        self.color = color
        self.size = size
        self.speed = speed

    # Membuat objek baru secara acak
    def create(self):
        rand_change = random.randint(1, 3)
        if rand_change == 1:
            new_object = Turtle()
            new_object.penup()
            new_object.shape(self.shape)
            if self.color:
                new_object.color(self.color)
            new_object.shapesize(*self.size)
            new_object.goto(random.randint(-300, 300), 360)
            new_object.left(90)  # Mengarahkan objek ke bawah
            self.objects.append(new_object)

    # Menggerakkan semua objek ke bawah
    def fall(self):
        for obj in self.objects:
            obj.backward(self.speed)

# Subkelas Asteroid dari Material
class Asteroid(Material):
    def __init__(self):
        # Asteroid memiliki atribut bawaan
        super().__init__(shape="asteroid.gif", color=None, size=(1, 2), speed=5)

class SpecialAsteroid(Material):
    def __init__(self, max_object=5):
        super().__init__(shape="special_asteroid.gif", color=None, size=(2, 3), speed=7)
        self.max_object = max_object  # Jumlah maksimum objek di layar

    # Membatasi jumlah objek di layar
    def create(self):
        self.clear_objects()  # Hapus objek yang keluar layar
        while len(self.objects) < self.max_object:
            super().create()
    # Menghapus objek di luar layar
    def clear_objects(self):
        self.objects = [obj for obj in self.objects if obj.ycor() > -360 and obj.isvisible()]


class Fuel(Material):
    def __init__(self):
        super().__init__(shape="fuel.gif", color=None, size=(0.5, 0.5), speed=10)
        self.collected = 0  # Menyimpan jumlah fuel yang dikumpulkan

    # Memberikan efek kebal jika fuel terkumpul cukup
    def boost_player(self, player):
        if self.collected >= 5:
            player.activate_invincibility()  # Aktifkan kebal
            self.collected = 0  # Reset jumlah fuel
