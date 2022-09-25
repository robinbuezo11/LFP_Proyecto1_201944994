import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from tkinter.filedialog import askopenfilename, asksaveasfile
from ManagerFile import ManagerFile

class WindowMain(ttk.Frame):
    def __init__(self, master, mfile=ManagerFile()) -> None:
        super().__init__(master)
        master.title('Proyecto 1')
        master.geometry('800x700')
        master.config(background='sky blue')
        master.resizable(False,False)
        self.__mfile = mfile

        self.__menu = tk.Menu()

        self.__menufile = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menufile, label='Archivo')

        self.__menufile.add_command(label='Abrir', command=self.__open)
        self.__menufile.add_command(label='Guardar', command=self.__save)
        self.__menufile.add_command(label='Guardar Como', command=self.__saveAs)
        self.__menufile.add_command(label='Analizar', command=self.__analyze)
        self.__menufile.add_command(label='Errores', command=self.__errors)
        self.__menufile.add_command(label='Salir', command=self.__exit)

        self.__menuhelp = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menuhelp, label='Ayuda')

        self.__menuhelp.add_command(label='Manual Técnico', command=self.__tecmanual)
        self.__menuhelp.add_command(label='Manual de Usuario', command=self.__usermanual)
        self.__menuhelp.add_command(label='Temas de Ayuda', command=self.__help)

        master.config(menu=self.__menu)

        self.__entrytext = tk.Text(master=master)
        self.__entrytext.place(x=20, y=20, width=760, height=660)

    def __open(self):
        try:
            self.__mfile.openFile()
            self.__entrytext.delete(1.0,'end')
            for line in self.__mfile.getData():
                self.__entrytext.insert('end', line)
        except Exception as e:
            msgbx.showerror('Error',e)

    def __save(self):
        try:
            self.__mfile.save(self.__entrytext.get(1.0,'end'))
        except Exception as e:
            msgbx.showerror('Error',e)

    def __saveAs(self):
        try:
            self.__mfile.save(self.__entrytext.get(1.0,'end'),True)
            self.__entrytext.delete(1.0,'end')
            for line in self.__mfile.getData():
                self.__entrytext.insert('end', line)
        except Exception as e:
            msgbx.showerror('Error',e)

    def __analyze(self):
            try:
                self.__mfile.analyzeText(self.__entrytext.get(1.0,'end'))
            except Exception as e:
                msgbx.showerror('Error',e)

    def __errors(self):
        msgbx.showinfo(message='Boton Errores')

    def __usermanual(self):
        msgbx.showinfo(message='Boton Manual Usuario')

    def __tecmanual(self):
        msgbx.showinfo(message='Boton Manual Tecnico')

    def __help(self):
        msgbx.showinfo('Ayuda','Desarrollador: Robin Omar Buezo Díaz\nCarne: 201944994\nCurso: Lenguajes Formales y De Programacion')

    def __exit(self):
        self.master.destroy()