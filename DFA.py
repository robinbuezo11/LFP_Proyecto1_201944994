
class DFA:
    def __init__(self,text=[]) -> None:
        self.__text = text
        self.__status = 0

    def analyze(self, text=[]):
        if text == []:
            text = self.__text
        errors =[]
        row = 1
        column = 1

        for line in text:
            column = 1
            self.__status = 0
            for char in line:
                if self.__status == 0:
                    self.__status0(char=char)
                elif self.__status == 1:
                    self.__status1(char=char)
                elif self.__status == 2:
                    self.__status2(char=char)
                elif self.__status == 3:
                    self.__status3(char=char)
                elif self.__status == 4:
                    self.__status4(char=char)
                elif self.__status == 5:
                    self.__status5(char=char)
                elif self.__status == 6:
                    self.__status6(char=char)
                elif self.__status == 7:
                    self.__status7(char=char)
                elif self.__status == 8:
                    self.__status8(char=char)
                elif self.__status == 9:
                    self.__status9(char=char)
                elif self.__status == 10:
                    self.__status10(char=char)
                elif self.__status == 11:
                    self.__status11(char=char)
                elif self.__status == 12:
                    self.__status12(char=char)    
                column+=1
            row +=1
            
    def __status0(self, char):
        pass

    def __status1(self, char):
        pass

    def __status2(self, char):
        pass

    def __status3(self, char):
        pass

    def __status4(self, char):
        pass

    def __status5(self, char):
        pass

    def __status6(self, char):
        pass

    def __status7(self, char):
        pass

    def __status8(self, char):
        pass

    def __status9(self, char):
        pass

    def __status10(self, char):
        pass

    def __status11(self, char):
        pass

    def __status12(self, char):
        pass

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text