from tkinter import messagebox as msgbx

from DFA import DFA

class ManagerFile:
    def __init__(self) -> None:
        self.__file = None
        self.__filelines = None

    #----------------------- Functions ----------------------------
    def openFile(self,ruta):   #Metodo para leer el archivo
        try:
            self.__file = open(ruta,'r', encoding='utf-8')
            self.__filelines = self.__file.readlines()
            
            msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
            
            self.__readFile(self.__filelines)
        except Exception:
            msgbx.showerror("ERROR",'Error en la carga, revise que los datos y la ruta de su archivo sean correctos.')
            if self.__file is not None:
                self.__file.close()


    def __readFile(self, file):     #Metodo para analizar el archivo
        dfa = DFA(file)
        dfa.analyze()

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

