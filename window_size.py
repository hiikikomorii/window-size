import tkinter as tk
last_size = None
fullscreen = False
try:
    import pygetwindow as gw
except ModuleNotFoundError:
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "Module pygetwindow not found\n", "Error", 0x10)
    exit()

class App:
    def __init__(self, main):
        self.main = main

    def window(self):
        global last_size

        win_gui = gw.getActiveWindow()
        size = "Нет активного окна"
        if win_gui:
            size = f"\r{win_gui.width}x{win_gui.height}"
            self.main.label.config(text=size)
            self.main.label.pack(anchor='n')
        else:
            pass

        if size != last_size:
            self.main.label.config(text=size)
            self.main.label.pack()
            last_size = size
        self.main.root.after(50, self.window)

    def set_font(self):
        try:
            set_font_bcnd = self.main.entryfont.get()

            if not set_font_bcnd:
                self.main.label_out.config(text=f"Введите число", fg="red")
                self.main.label_out.pack()
                return

            self.main.label.config(font=("Arial", set_font_bcnd))
            self.main.entryfont.delete(0, 'end')
            self.main.label_out.config(text="Font changed successfully", fg="green", font=12)
            self.main.label_out.pack()
        except Exception as er:
            self.main.label_out.config(text=f"Введите число\n{er}", fg="red")
            self.main.label_out.pack()

class Main:
    def __init__(self, master):
        self.root = master
        self.root.geometry("400x300")
        self.root.title("py-get-window")

        self.app = App(self)
        self._widgets()
        self.app.window()

        self.fscr_btn.config(fg="red")

    def _widgets(self):
        self.frame_set = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.main_btn_frame = tk.Frame(self.root)
        self.main_btn_frame.pack()

        self.label_guide = tk.Label(self.frame_set, text="Введите размер шрифта")
        self.label_guide.pack(anchor="n")
        self.entryfont = tk.Entry(self.frame_set)
        self.entryfont.pack()

        self.settings_button = tk.Button(self.main_btn_frame, bg="lightgray", text="Font", width=5, command=self.settings)
        self.settings_button.pack(anchor="s", side="left")
        self.fscr_btn = tk.Button(self.main_btn_frame, bg="lightgray", text="Fullscreen", width=8, command=self.toggle_fullscreen)
        self.fscr_btn.pack(anchor="s", side="left", padx=10)
        self.exit_button = tk.Button(self.main_btn_frame, fg="white", bg="red", text="Exit", width=5, command=exit)
        self.exit_button.pack(anchor="s", side="left")

        self.apply_btn = tk.Button(self.frame_set, text="Set", fg="white", bg="green", width=10, command=self.app.set_font).pack(pady=10)
        self.back = tk.Button(self.frame_set, text="Back", fg="white", bg="red", width=10, command=self.back_to_main).pack()

        self.label = tk.Label(self.main_frame, font=("Arial", 30))
        self.label_out = tk.Label(self.frame_set, fg="red", font=("Arial", 20))

    def toggle_fullscreen(self):
        global fullscreen
        fullscreen = not fullscreen
        self.root.attributes("-fullscreen", fullscreen)
        if fullscreen:
            self.root.attributes("-fullscreen", True)
            self.fscr_btn.configure(fg="#00CF00")
        else:
            self.root.attributes("-fullscreen", False)
            self.fscr_btn.configure(fg="#CF0000")

    def back_to_main(self):
        self.frame_set.pack_forget()
        self.main_frame.pack()
        self.main_btn_frame.pack()
        self.label_out.pack_forget()

    def settings(self):
        self.entryfont.delete(0, 'end')
        self.main_btn_frame.pack_forget()
        self.main_frame.pack_forget()
        self.frame_set.pack()
        self.label_out.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    mainapp = Main(root)
    root.mainloop()