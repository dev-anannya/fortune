import tkinter as tk
import random
from fortune import getFortunes

class FortuneTellerApp:
    def __init__(self, master):
        self.master = master
        master.title("Fortune Teller")

        self.fortunes = getFortunes()
        self.fortune_count = 0
        self.max_fortunes_per_day = 10

        self.label = tk.Label(master, text="Click the button to generate your fortune!")
        self.label.pack(pady=10)

        self.fortune_text = tk.Text(master, height=10, width=50)
        self.fortune_text.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate Fortune", command=self.generate_fortune)
        self.generate_button.pack(pady=10)

    def generate_fortune(self):
        if self.fortune_count < self.max_fortunes_per_day:
            # Clear previous fortune
            self.fortune_text.delete('1.0', tk.END)
            
            # Generate a new fortune
            fortune = random.choice(self.fortunes)
            self.fortune_text.insert(tk.END, fortune + "\n")
            self.fortune_count += 1
        else:
            self.label.config(text="You've reached the limit of 10 fortunes for today.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FortuneTellerApp(root)
    root.mainloop()
