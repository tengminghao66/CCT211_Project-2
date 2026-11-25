import tkinter as tk
from clothing_form import ClothingForm

class DigitalWardrobe(tk.Tk):
    def __init__(self):
        super().__init__()

        # main window settings
        self.title("Digital Wardrobe")
        self.geometry("600x450")
        self.resizable(False, False)

        # creating the interface
        self.create_widgets()
        
    def create_widgets(self):
        # title 
        title_label = tk.Label(
            self,
            text="Digital Wardrobe",
            font=("Arial", 22, "bold")
        )
        title_label.pack(pady=30)

        # wardrobe button
        wardrobe_button = tk.Button(
            self,
            text="My Wardrobe",
            width=25,
            height=2,
            command=self.open_wardrobe
        )
        wardrobe_button.pack(pady=10)

        # add clothing button
        add_button = tk.Button(
            self,
            text="Add Clothing",
            width=25,
            height=2,
            command=self.open_add_clothing
        )
        add_button.pack(pady=10)

        # add outfit button
        outfit_button = tk.Button(
            self,
            text="My Outfits",
            width=25,
            height=2,
            command=self.open_outfits
        )
        outfit_button.pack(pady=10)

    def open_wardrobe(self):
        wardrobe_window = tk.Toplevel(self)
        wardrobe_window.title("My Wardrobe")
        wardrobe_window.geometry("500x400")  

        tk.Label(
            wardrobe_window,
            text="My Wardrobe",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

    def open_add_clothing(self):
        ClothingForm(self)

    def open_outfits(self):
        outfit_window = tk.Toplevel(self)
        outfit_window.title("My Outfits")
        outfit_window.geometry("500x400")

        tk.Label(
            outfit_window,
            text="My Outfits",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

if __name__ == "__main__":
    app = DigitalWardrobe()
    app.mainloop()