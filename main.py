import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        
        # Window Size
        self.root.geometry('800x600') 
        
        # Title of the window
        self.root.title("Typing Speed Test")

        # Main Frame
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)


        # Widget
        self.text = ttk.Label(self.mainframe, text="Typing Speed Test", background='white', font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')

        self.root.mainloop()        
        return
    
if __name__ == '__main__':
    App()
