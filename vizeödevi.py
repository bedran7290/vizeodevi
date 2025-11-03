
"""
Created on Sun Nov  2 14:55:13 2025

@author: HP
"""

import tkinter as tk
import time

class TrafikIsigiSimulasyon:
    def __init__(self, root):
        self.root = root
        self.root.title("🚦 LED Trafik Işığı Simülasyonu")
        self.root.config(bg="black")
        self.root.geometry("220x420")

        # Tuval (ışıkların çizildiği alan)
        self.canvas = tk.Canvas(root, width=200, height=400, bg="gray20", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Gövde
        self.canvas.create_rectangle(60, 30, 140, 370, fill="black", outline="gray70", width=4)

        # Işıklar (LED’ler)
        self.red = self.canvas.create_oval(70, 50, 130, 110, fill="gray25")
        self.yellow = self.canvas.create_oval(70, 160, 130, 220, fill="gray25")
        self.green = self.canvas.create_oval(70, 270, 130, 330, fill="gray25")

        # Durum etiketi
        self.label = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 12, "bold"))
        self.label.pack(pady=5)

        # Başlat butonu
        self.start_button = tk.Button(root, text="▶ Başlat", command=self.start_simulation,
                                      bg="green", fg="white", font=("Arial", 12, "bold"), width=10)
        self.start_button.pack(pady=5)

        self.running = False

        # Süreler (saniye)
        self.red_time = 4
        self.yellow_time = 2
        self.green_time = 2

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.start_button.config(state="disabled")
            self.simulate_cycle()

    def simulate_cycle(self):
        if not self.running:
            return

        # 🔴 KIRMIZI — DUR
        self.update_lights("red")
        self.label.config(text="KIRMIZI — DUR", fg="red")
        self.root.update()
        time.sleep(self.red_time)

        # 🟡 SARI — HAZIRLAN
        self.update_lights("yellow")
        self.label.config(text="SARI — HAZIRLAN", fg="yellow")
        self.root.update()
        time.sleep(self.yellow_time)

        # 🟢 YEŞİL — GEÇ
        self.update_lights("green")
        self.label.config(text="YEŞİL — GEÇ", fg="lime")
        self.root.update()
        time.sleep(self.green_time)

        # Döngü tekrar başa dönüyor
        self.simulate_cycle()

    def update_lights(self, color):
        # Önce tüm ışıkları kapat
        self.canvas.itemconfig(self.red, fill="gray25")
        self.canvas.itemconfig(self.yellow, fill="gray25")
        self.canvas.itemconfig(self.green, fill="gray25")

        # Seçilen rengi yak
        if color == "red":
            self.canvas.itemconfig(self.red, fill="red")
        elif color == "yellow":
            self.canvas.itemconfig(self.yellow, fill="yellow")
        elif color == "green":
            self.canvas.itemconfig(self.green, fill="lime")

# === Uygulamayı Başlat ===
root = tk.Tk()
app = TrafikIsigiSimulasyon(root)
root.mainloop()
