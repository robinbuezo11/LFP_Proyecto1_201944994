import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx

class WindowMain(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        master.title('Proyecto 1')
        master.geometry('800x700')
        master.config(background='sky blue')
        master.resizable(False,False)

        menu = tk.Menu()

        menufile = tk.Menu(menu, tearoff=False)
        menu.add_cascade(menu=menufile, label='Archivo')

        menufile.add_command(label='Abrir', command=self.__open)
        menufile.add_command(label='Guardar', command=self.__open)
        menufile.add_command(label='Guardar Como', command=self.__open)
        menufile.add_command(label='Analizar', command=self.__open)
        menufile.add_command(label='Errores', command=self.__open)
        menufile.add_command(label='Salir', command=self.__open)

        menuhelp = tk.Menu(menu, tearoff=False)
        menu.add_cascade(menu=menuhelp, label='Ayuda')

        menuhelp.add_command(label='Manual Técnico', command=self.__open)
        menuhelp.add_command(label='Manual de Usuario', command=self.__open)
        menuhelp.add_command(label='Temas de Ayuda', command=self.__open)

        master.config(menu=menu)

        entrytext = ttk.Entry(master=master)
        entrytext.place(x=20, y=20, width=760, height=660)

    def __open(self):
        msgbx.showinfo('Info','Has presionado el boton de abrir')