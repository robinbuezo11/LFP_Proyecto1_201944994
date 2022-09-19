import tkinter as tk
from tkinter import ttk

class WindowMain(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        master.title('Proyecto 1')
        master.geometry('700x550')
        master.config(background='sky blue')
        master.resizable(False,False)