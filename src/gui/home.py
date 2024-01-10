import customtkinter as CTk
from gui import typePage

class Home(CTk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.label = CTk.CTkLabel(self, text="Home", font=("Roboto", 24))
        self.label.pack(padx=20, pady=20)

        self.button = CTk.CTkButton(self, text="Start Typing!", command=self.switch_page, 
                                     fg_color="#4158D0", border_color="#FFCC70", hover_color="#C850C0",
                                     corner_radius=20, font=("Roboto", 24))
        self.button.pack(padx=20, pady=20)

    def switch_page(self):
        self.master.show_frame(typePage.TypePage)
