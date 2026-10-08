import tkinter as tk
from tkinter import ttk
from tkinter import font

class FancyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.expression = ""

        # Custom font
        self.display_font = font.Font(family="Consolas", size=24, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=14)

        # Entry widget for display
        self.entry = tk.Entry(root, font=self.display_font, bg="#ecf0f1", bd=10,
                              relief=tk.RIDGE, justify="right", fg="#2c3e50")
        self.entry.pack(padx=10, pady=20, fill="both")

        # Button layout
        buttons = [
            ['C', '⌫', '', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        for row in buttons:
            row_frame = tk.Frame(self.root, bg="#2c3e50")
            row_frame.pack(expand=True, fill="both", padx=10, pady=5)
            for char in row:
                if char:
                    self.create_button(row_frame, char)
                else:
                    tk.Label(row_frame, text="", bg="#2c3e50").pack(side="left", expand=True, fill="both")

    def create_button(self, frame, char):
        btn = tk.Button(
            frame,
            text=char,
            font=self.button_font,
            bg="#34495e",
            fg="white",
            activebackground="#1abc9c",
            activeforeground="white",
            bd=0,
            relief=tk.FLAT,
            command=lambda ch=char: self.on_click(ch)
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = FancyCalculator(root)
    root.mainloop()
