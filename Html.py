
class Html:
    def __init__(self, errors=[], tokens=[]) -> None:
        self.__errors = errors
        self.__tokens = tokens

    def generateErrors(self):
        text='<!DOCTYPE html><html><body><div style="text-align:center"><h1>Tabla de Errores</h1>'
        text+='<table border=1 style="margin: 0 auto;" class="default">'
        text+='<tr><th>No.</th><th>Lexema</th><th>Tipo</th><th>Columna</th><th>Fila</th></tr>'
        iterator=0
        for error in self.__errors:
            text+=f'<tr><td>{iterator}</td><td>{error[0]}</td><td>Error</td><td>{error[2]}</td><td>{error[1]}</td></tr>'
            iterator+=1
        text+='</table></div></body></html>'

        file=open('./ERRORES_201944994.html','w',encoding='utf-8')
        file.write(text)
        file.close()

    def generateResults(self):
        text = '<!DOCTYPE html><html><body><div style="text-align:center"><h1>Tabla de Errores</h1>'

    def operations(self):
        pass