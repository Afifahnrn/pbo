import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemutar Video")

        self.video_path = "C:/Users/nurkh/OneDrive/Documents/AFIFAH NURAINI/PBO/pertemuan 7/tugas/Animasi.mp4"

        self.canvas = tk.Canvas(root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.label_status = tk.Label(root, text=f"File Video: {self.video_path}", pady=10)
        self.label_status.pack()

        self.button_play = tk.Button(root, text="Putar", command=self.play_video)
        self.button_play.pack(side=tk.LEFT, padx=10)

        self.button_stop = tk.Button(root, text="Stop", command=self.stop_video)
        self.button_stop.pack(side=tk.RIGHT, padx=10)

        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            self.cap = None
            self.label_status.config(text="Error: Tidak dapat membuka file video")

    def play_video(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.photo = self.convert_frame_to_photo(frame)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                self.root.after(10, self.play_video)
            else:
                self.label_status.config(text="Selesai memutar video")
                self.cap.release()

    def stop_video(self):
        if self.cap:
            self.cap.release()
            self.canvas.delete("all")

    def convert_frame_to_photo(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(img)
        return img

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
