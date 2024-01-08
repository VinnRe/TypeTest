from gui import home
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")

        self._set_appearance_mode("dark")

        self.showFrame(home.Home)

    def showFrame(self, frame_class):
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()
        frameInstance = frame_class(self)
        frameInstance.pack(padx=20, pady=20)
        self.current_frame = frameInstance

app = App()
app.mainloop()
