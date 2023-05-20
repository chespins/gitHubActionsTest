import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('テストツール')
        self.master.geometry('500x250')
        self.master.resizable(False, False)
 
        frame1 = tk.Frame(self.master, width=500, height=90, borderwidth=2, relief='solid')
        frame2 = tk.Frame(self.master, width=500, height=40, borderwidth=2, relief='solid')
        frame3 = tk.Frame(self.master, width=500, height=120, borderwidth=2, relief='solid')
    
        frame1.propagate(False)
        frame2.propagate(False)
        frame3.propagate(False) 
        
        frame1.grid(row=0, column=0)
        frame2.grid(row=1, column=0)
        frame3.grid(row=2, column=0)
 
        # frame
        self.button_quit = tk.Button(frame3, text='終了', command=sys.exit)
        self.button_quit.pack(side=tk.TOP)


def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == '__main__':
    main()
