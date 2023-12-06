import pygame
from tkinter import Tk, Button, Label

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Ganti path file MP3 sesuai dengan lokasi file
        self.music_file = self.music_file = "C:/Users/nurkh/OneDrive/Documents/AFIFAH NURAINI/PBO/pertemuan 6/tugas/angel.mp3"

        self.label_artist = Label(root, text="AFIFAH NURAINI 220511027")
        self.label_artist.pack(pady=20, padx=5)

        self.label_song = Label(root, text="EXO : angel")
        self.label_song.pack(pady=10, padx=5)

        self.button_play = Button(root, text="Play Music", command=self.play_music)
        self.button_play.pack(pady=20)

        self.button_stop = Button(root, text="Stop Music", command=self.stop_music)
        self.button_stop.pack(pady=10)

        # Inisialisasi mixer pygame
        pygame.mixer.init()

    def play_music(self):
        # Memeriksa apakah musik sedang diputar
        if pygame.mixer.music.get_busy():
            print("Music is already playing.")
        else:
            # Memutar musik
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def stop_music(self):
        # Menghentikan pemutaran musik
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
