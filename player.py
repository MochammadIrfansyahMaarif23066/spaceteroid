from turtle import Turtle
import time

# Posisi awal pemain
POS_X = 0
POS_Y = -280

class Player:
    def __init__(self):
        self.fly = Turtle()  # Objek pemain
        self.fly.penup()
        self.fly.shape("player.gif")
        self.fly.color("green")
        self.fly.shapesize(1, 3)
        self.fly.goto(POS_X, POS_Y)
        self.fly.left(90)  # Menghadap ke atas

        self.invincible = False  # Status kebal pemain
        self.invincible_start_time = 0  # Waktu mulai kebal
        self.invincible_duration = 5  # Durasi kebal dalam detik

        # Menampilkan timer invincibility di layar
        self.timer_display = Turtle()
        self.timer_display.hideturtle()
        self.timer_display.penup()
        self.timer_display.color("white")
        self.timer_display.goto(-270, 220)
        self.show_invincibility_status()

    # Gerakan ke kanan
    def move_right(self):
        pos_x = self.fly.xcor()
        new_pos = pos_x + 10
        self.fly.goto(x=new_pos, y=POS_Y)
        if self.fly.xcor() > 380:  # Cek jika keluar batas kanan layar
            new_pos = pos_x
            self.fly.goto(x=new_pos, y=POS_Y)

    # Gerakan ke kiri
    def move_left(self):
        pos_x = self.fly.xcor()
        new_pos = pos_x - 10
        self.fly.goto(x=new_pos, y=POS_Y)
        if self.fly.xcor() < -380:  # Cek jika keluar batas kiri layar
            new_pos = pos_x
            self.fly.goto(x=new_pos, y=POS_Y)
    def show_invincibility_status(self):
        """Tampilkan status invincibility di layar."""
        self.timer_display.clear()  # Bersihkan tampilan sebelumnya
        if self.invincible:
            time_left = max(0, int(self.invincible_duration - (time.time() - self.invincible_start_time)))
            self.timer_display.write(f"Invincibility: {time_left}", align="center", font=("Arial", 18, "bold"))
        else:
            self.timer_display.write("Invincibility: 0", align="center", font=("Arial", 18, "bold"))

    def activate_invincibility(self):
        """Aktifkan invincibility."""
        self.invincible = True
        self.invincible_start_time = time.time()  # Catat waktu mulai
        self.show_invincibility_status()  # Perbarui tampilan

    def check_invincibility(self):
        """Cek apakah invincibility masih aktif."""
        if self.invincible:
            time_left = self.invincible_duration - (time.time() - self.invincible_start_time)
            if time_left <= 0:
                self.invincible = False  # Matikan invincibility jika waktu habis
                self.fly.shape("player.gif")  # Reset bentuk pemain
            self.show_invincibility_status()  # Perbarui tampilan
