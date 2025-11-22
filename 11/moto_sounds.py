import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

current_img = None

def show_image(file, label):
    global current_img
    img = Image.open(file)
    img = img.resize((300, 200))
    current_img = ImageTk.PhotoImage(img)
    label.config(image=current_img)

def create_app():
    root = tk.Tk()
    root.title("Moto Exhaust Sounds")
    root.geometry('370x600')
    root.resizable(False, False)


    image_label = tk.Label(root)
    image_label.pack()

    # Кнопка BMW S1000RR
    tk.Button(root, text="Bmw S1000RR", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("sounds/s1000rr.mp3")),
                               show_image(abs_path("photos/s1000rr.jpg"), image_label)]
             ).pack(pady=10)

    #r1
    tk.Button(root, text="Yamaha YZF-R1", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("sounds/yamaha-r1.mp3")),
                               show_image(abs_path("photos/r1.jpg"), image_label)]
              ).pack(pady=10)

    #r6
    tk.Button(root, text="Yamaha YZF-R6", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("sounds/yamaha-r6.mp3")),
                               show_image(abs_path("photos/r6.jpg"), image_label)]
              ).pack(pady=10)

    #cbr1000
    tk.Button(root, text="Honda CBR-1000RR", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("sounds/cbr-1000.mp3")),
                               show_image(abs_path("photos/cbr1000.jpg"), image_label)]
              ).pack(pady=10)

    #h2r
    tk.Button(root, text="Kawasaki Ninja H2R", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("sounds/kawasaki_h2r.mp3")),
                               show_image(abs_path("photos/h2r.jpg"), image_label)]
              ).pack(pady=10)

    root.mainloop()

create_app()
