import customtkinter as CTk
import time
import threading
import random
import pkg_resources

# Access the texts.txt from resources folder
texts_content = pkg_resources.resource_string(__name__, '../resources/texts.txt').decode('utf-8')
texts = texts_content.split("\n")

class TypePage(CTk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.title_label = CTk.CTkLabel(self, text="Typing Page", font=("Roboto", 24))
        self.title_label.pack(padx=20, pady=20)

        self.sample_label = CTk.CTkLabel(self, text=random.choice(texts), font=("Roboto", 24))
        self.sample_label.pack(padx=20, pady=20)

        self.input_entry = CTk.CTkEntry(self, width=600, font=("Roboto", 30))
        self.input_entry.pack(padx=20, pady=20)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = CTk.CTkLabel(self, text="Speed: \n0.00 CPS\n0.00 CPM\n 0.00 WPS\n 0.00 WPM", font=("Roboto", 24))
        self.speed_label.pack(padx=20, pady=20)

        self.reset_button = CTk.CTkButton(self, text="Reset", command=self.reset, font=("Roboto", 24))
        self.reset_button.pack(padx=20, pady=20)

        self.coutner = 0
        self.running = False

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.configure(text_color="red")
        else:
            self.input_entry.configure(text_color="white")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.configure(text_color="green")


    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.coutner += 0.1
            cps = len(self.input_entry.get()) / self.coutner
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.coutner
            wpm = wps * 60
            self.speed_label.configure(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f} WPS\n {wpm:.2f} WPM")


    def reset(self):
        self.running = False
        self.coutner = 0
        self.speed_label.configure(text="Speed: \n0.00 CPS\n0.00 CPM\n 0.00 WPS\n 0.00 WPM")
        self.sample_label.configure(text=random.choice(texts))
        self.input_entry.delete(0, CTk.END)