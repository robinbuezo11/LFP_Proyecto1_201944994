from tkinter import messagebox as msgbx

from DFA import DFA

class ManagerFile:
    def __init__(self) -> None:
        self.__data = []

    #----------------------- Functions ----------------------------
    def openFile(self,ruta):   #Metodo para leer el archivo
        try:
            file = open(ruta,'w+', encoding='utf-8')
            self.__data = file.readlines()
            
            msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
            
            self.__readFile(self.__data)
        except Exception:
            msgbx.showerror("ERROR",'Error en la carga, revise que los datos y la ruta de su archivo sean correctos.')
            if file is not None:
                file.close()

    def __readFile(self, filelines=[]):     #Metodo para analizar el archivo
        dfa = DFA()
        dfa.analyze(filelines)

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

