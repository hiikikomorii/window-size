import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("py-get-window")
last_size = None
fullscreen = False

def window():
    global last_size
    try:
        import pygetwindow as gw
    except ModuleNotFoundError:
        import ctypes
        import sys
        ctypes.windll.user32.MessageBoxW(0, "Module pygetwindow not found\n", "Error", 0x10)
        sys.exit()

    win_gui = gw.getActiveWindow()
    size = "Нет активного окна"
    if win_gui:
        size = f"\r{win_gui.width}x{win_gui.height}"
        label.config(text=size)
        label.pack(anchor='n')
    else:
        pass

    if size != last_size:
        label.config(text=size)
        label.pack()
        last_size = size
    root.after(50, window)


def back_to_main():
    frame_set.pack_forget()
    main_frame.pack()
    main_btn_frame.pack()
    label_out.pack_forget()

def settings():
    entryfont.delete(0, 'end')
    main_btn_frame.pack_forget()
    main_frame.pack_forget()
    frame_set.pack()
    label_out.pack_forget()

def set_font():
    try:
        set_font_bcnd = entryfont.get()

        if not set_font_bcnd:
            label_out.config(text=f"Введите число", fg="red")
            label_out.pack()
            return

        label.config(font=("Arial", set_font_bcnd))
        entryfont.delete(0, 'end')
        label_out.config(text="Font changed successfully", fg="green", font=12)
        label_out.pack()
    except Exception as er:
        label_out.config(text=f"Введите число\n{er}", fg="red")
        label_out.pack()

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    if fullscreen:
        root.attributes("-fullscreen", True)
        fscr_btn.configure(fg="#00CF00")
    else:
        root.attributes("-fullscreen", False)
        fscr_btn.configure(fg="#CF0000")


frame_set = tk.Frame(root)
main_frame = tk.Frame(root)
main_frame.pack()
main_btn_frame = tk.Frame(root)
main_btn_frame.pack()

label_guide = tk.Label(frame_set, text="Введите размер шрифта")
label_guide.pack(anchor="n")
entryfont = tk.Entry(frame_set)
entryfont.pack()


settings_button = tk.Button(main_btn_frame, bg="lightgray", text="Font", width=5, command=settings)
settings_button.pack(anchor="s", side="left")
fscr_btn = tk.Button(main_btn_frame, bg="lightgray", text="Fullscreen", width=8, command=toggle_fullscreen)
fscr_btn.pack(anchor="s", side="left", padx=10)
exit_button = tk.Button(main_btn_frame, fg="white", bg="red", text="Exit", width=5, command=exit)
exit_button.pack(anchor="s", side="left")


apply_btn = tk.Button(frame_set, text="Set", fg="white", bg="green", width=10, command=set_font).pack(pady=10)
back = tk.Button(frame_set, text="Back", fg="white", bg="red", width=10, command=back_to_main).pack()

label = tk.Label(main_frame, font=("Arial", 30))
label_out = tk.Label(frame_set, fg="red", font=("Arial", 20))

window()
root.mainloop()