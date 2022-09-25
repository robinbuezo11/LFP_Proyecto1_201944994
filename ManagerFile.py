from tkinter import messagebox as msgbx
from tkinter.filedialog import askopenfilename, asksaveasfile

from DFA import DFA

class ManagerFile:
    def __init__(self) -> None:
        self.__path = None
        self.__data = []

    #----------------------- Functions ----------------------------
    def openFile(self):   #Metodo para leer el archivo
        try:
            path = askopenfilename()
            file = open(path,'r', encoding='utf-8')
            self.__path = path
            if file is not None:
                self.__data = file.readlines()
                file.close()
            msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
        except Exception:
            if file is not None:
                file.close()
            msgbx.showerror("ERROR",'Error en la carga, revise que los datos y la ruta de su archivo sean correctos.')

    def analyzeText(self, filelines=[]):     #Metodo para analizar el archivo
        dfa = DFA()
        dfa.analyze(filelines)

    def save(self,data,saveas=False):
        try:
            if saveas:
                file = asksaveasfile(title='Guardar como',defaultextension='.txt', filetypes=[('Todos','*.*')],mode='w')
            else:
                file = open(self.__path,'w', encoding='utf-8')
            file.write(data)
            file.close()
            msgbx.showinfo('Guardado','Archivo guardado exitosamente')
        except Exception as e:
            if file is not None:
                file.close()
            msgbx.showerror("ERROR",e)

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path


