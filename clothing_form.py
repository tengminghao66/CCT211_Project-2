import tkinter as tk
from tkinter import ttk, messagebox


class ClothingForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Add Clothing")
        self.geometry("450x400")

        # form title
        tk.Label(
            self,
            text="Add New Clothing",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # clothing name
        tk.Label(self, text="Clothing Name:").pack()
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.pack(pady=5)

        # category
        tk.Label(self, text="Category:").pack()
        self.category_box = ttk.Combobox(
            self,
            values=["Top", "Bottoms", "Shoes", "Outerwear", "Accessories"],
            state="readonly",
            width=27
        )
        self.category_box.pack(pady=5)

        # colour
        tk.Label(self, text="Colour:").pack()
        self.colour_entry = tk.Entry(self, width=30)
        self.colour_entry.pack(pady=5)

        # season
        tk.Label(self, text="Season:").pack()
        self.season_box = ttk.Combobox(
            self,
            values=["Spring", "Summer", "Autumn", "Winter"],
            state="readonly",
            width=27
        )
        self.season_box.pack(pady=5)

        # save button
        tk.Button(
            self, 
            text="Save Clothing",
            command=self.save_clothing
        ).pack(pady=20)

    def save_clothing(self):
        name = self.name_entry.get().strip()
        category = self.category_box.get()
        colour = self.colour_entry.get().strip()
        season = self.season_box.get()

        # to check if all fields are completed
        if not name or not category or not colour or not season:
            messagebox.showerror(
                "Missing Information",
                "Please fill in all fields before saving.",
                parent=self
            )
            return 

        # place holder until the database in implemented
        print("Clothing Name:", name)
        print("Category:", category)
        print("Colour:", colour)
        print("Season:", season)

        messagebox.showinfo(
            "Success",
            "Clothing item saved successfully!",
            parent=self            
        )
