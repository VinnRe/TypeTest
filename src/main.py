from gui import home
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Typing Test Challenge")
        self._set_appearance_mode("dark")

        self.show_frame(home.Home)

    def show_frame(self, frame_class):
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()
        frame_instance = frame_class(self)
        frame_instance.pack(padx=20, pady=20)
        self.current_frame = frame_instance

app = App()
app.mainloop()
