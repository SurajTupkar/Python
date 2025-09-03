"""
private DM & MF

"""

class Student:
    __name="Ann"


    def __key(self):
        print("This is private Key method")

    def getname(self,name):
        self.__name= name
        print(self.__name)

    def getkey(self):
        self.__key()
    



obj=Student()
# print(obj.__name)
obj.getname("suraj")
obj.getkey()


