from turtle import Turtle

class Board(Turtle):
    """Kelas untuk mengelola skor pemain dan highscore."""
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            # Membaca skor tertinggi dan skor terakhir dari file
            with open("highscore.txt") as data:
                content = data.read().splitlines()
                self.high_score = int(content[0].split('=')[1])  # highscore=...
                self.last_score = int(content[1].split('=')[1])  # last_score=...
        except FileNotFoundError:
            # Jika file tidak ditemukan, buat file baru dengan skor awal 0
            with open("highscore.txt", mode="w") as data:
                self.high_score = 0
                self.last_score = 0
                data.write(f"highscore={self.high_score}\nlast_score={self.last_score}")
        finally:
            # Mengatur properti turtle untuk papan skor
            self.penup()
            self.hideturtle()
            self.color("red")

    # Metode untuk memperbarui tampilan papan skor
    def update_board(self):
        self.goto(x=-350, y=250)  # Posisi papan skor di layar
        self.write(arg=f"Score: {self.score}\nHighScore: {self.high_score}", font=("Arial", 18, "bold"))

    # Metode untuk menambah skor pemain
    def increase_score(self):
        self.score += 50  # Menambahkan 50 poin ke skor
       
        self.clear()  # Membersihkan tampilan lama
        self.update_board()  # Memperbarui papan skor

    def save_scores(self):
        """Menyimpan highscore dan last_score ke dalam file"""
        self.last_score = self.score
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highscore.txt", mode="w") as data:
            data.write(f"highscore={self.high_score}\nlast_score={self.last_score}")
