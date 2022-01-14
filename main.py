import tkinter as tk
import time

window = tk.Tk()


def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("pm")
    time_text = f"{hours}:{minutes}:{seconds} {am_or_pm}"
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = tk.Label(window, text="00: 00: 00",
                             font="Helvetica 72 bold"
                             )
digital_clock_lbl.pack()
update_clock()