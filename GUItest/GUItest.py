import tkinter as tk
import os

def newtxt_func():
    dir = os.path.dirname(__file__)
    datafile = open(dir + "/newtxt.txt", "w+")
    test = "ok?"
    datafile.write(test)
    datafile.close()

Px = 350/2
Py = 350/2

root = tk.Tk()
root.geometry("350x350")

run_botton = tk.Button(root, text = "Run", command = newtxt_func)
run_botton.place(x = Px-10, y = Py)

set_botton = tk.Button(root, text = "Set")
set_botton.place(x = Px+125, y = Py-25)

input_box = tk.Entry(width = 40)
input_box.place(x = Px-120, y = Py-20)

statusbar = tk.Label(root, text = " NO DATA!!", bd = 1, relief = tk.RAISED, anchor = tk.E)
statusbar.pack(side = tk.BOTTOM, fill = tk.X)

root.mainloop()

