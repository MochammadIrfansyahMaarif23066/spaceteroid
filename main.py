from turtle import Screen
from player import Player
from material import Asteroid, SpecialAsteroid, Fuel
from score import Board
from menu import StartMenu, GameOverMenu
import time

screen = Screen()
game_speed = 0.05

def start_game():
    global player, asteroid, special_asteroid, fuel, board, is_on
    screen.clear()  # Bersihkan layar
    screen.bgcolor("black")
    screen.tracer(0)

    # Inisialisasi gambar
    screen.addshape("player.gif")
    screen.addshape("asteroid.gif")
    screen.addshape("special_asteroid.gif")
    screen.addshape("fuel.gif")

    # Inisialisasi objek game
    player = Player()
    asteroid = Asteroid()
    special_asteroid = SpecialAsteroid()
    fuel = Fuel()
    board = Board()
    board.update_board()  # Tampilkan skor awal
    is_on = True  # Set status game aktif

    # Atur kontrol pemain
    screen.listen()
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(player.move_left, "Left")

    # Jalankan game loop
    main_game_loop()

# Fungsi untuk restart game setelah game over.
def restart_game():
    global is_on
    is_on = False
    time.sleep(1)
    start_game()

# Fungsi untuk keluar dari game.
def quit_game():
    screen.bye()

# Tampilkan menu awal dengan highscore dan opsi untuk mulai atau keluar.
def show_start_menu():
    highscore, last_score = Board().high_score, Board().last_score
    start_menu = StartMenu(screen, highscore, last_score)
    start_menu.activate({
        "Start": start_game,
        "Exit": quit_game
    })

# Tampilkan menu game over dengan skor akhir dan opsi restart atau keluar.
def show_game_over_menu():
    global is_on
    is_on = False
    
    board.save_scores()# Simpan skor saat game over
    game_over_menu = GameOverMenu(screen, board.score)
    game_over_menu.show_animation()  # Animasi saat game over
    game_over_menu.activate({
        "Restart": restart_game,
        "Exit": quit_game
    })
# Fungsi utama untuk menjalankan game loop dan mengatur logika permainan
def main_game_loop():
    global is_on
    while is_on:
        screen.update()  # Perbarui layar
        time.sleep(game_speed)  # Delay untuk kecepatan game

        # Proses objek game
        asteroid.create()
        asteroid.fall()
        special_asteroid.fall()
        fuel.create()
        fuel.fall()

        # Deteksi jika fuel diambil pemain
        for square in fuel.objects:
            if square.distance(player.fly) < 25:
                square.goto(1000, 1000) # Hilangkan fuel dari layar
                board.increase_score()
                fuel.collected += 1
                fuel.boost_player(player)

        # Periksa status kebal pemain
        player.check_invincibility()

        # Jika tidak kebal, periksa tabrakan
        if not player.invincible:
            for one_asteroid in asteroid.objects:
                if one_asteroid.distance(player.fly) < 20:
                    is_on = False

            for special in special_asteroid.objects:
                if special.distance(player.fly) < 20:
                    is_on = False

        # Tingkatkan kecepatan asteroid berdasarkan skor
        if board.score >= 200:
            asteroid.speed = 10
        if board.score >= 500:
            asteroid.speed = 15
            special_asteroid.create()
        if board.score >= 1000:
            asteroid.speed = 25
        if board.score >= 2500:
            asteroid.speed = 35

    # Jika loop berhenti, tampilkan menu game over
    show_game_over_menu()

# Inisialisasi layar
screen.setup(width=800, height=640)  # Atur ukuran layar
screen.bgcolor("black")
screen.tracer(0)

# Tampilkan menu awal
show_start_menu()
screen.mainloop()
