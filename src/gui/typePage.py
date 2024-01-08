import customtkinter as CTk

class TypePage(CTk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.label = CTk.CTkLabel(self, text="Typing Page", font=("Roboto", 24))
        self.label.pack(padx=20, pady=20)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.textbox = CTk.CTkTextbox(master=self, width=400, height=500, corner_radius=2)
        # self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.pack(padx=20, pady=20)
        self.textbox.insert("0.0", "")