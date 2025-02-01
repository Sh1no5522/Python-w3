class Str:
    def __init__(self , string):
        self.string = string
    
    def getString(self):
        print(self.string)
    
    def printString(self):
        print(self.string.upper())

b = input("Enter a string: ")    
str1 = Str(b)
str1.getString()
str1.printString()