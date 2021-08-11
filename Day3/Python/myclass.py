#!/usr/bin/python3

class MyClass:

    def __init__(self):
        print ( "Inside MyClass constructor ...")
        self.x = 0
        self.y = 0

    def setValues(self, value1, value2):
        print ( "Inside MyClass setValues ...")
        self.x = value1
        self.y = value2


    def printValues(self):
        print ("Inside printValues ...")
        print ( "x = ", self.x )
        print ( "y = ", self.y )

if __name__ == "__main__":

   obj = MyClass()

   print ( "MyClass values before calling setValues ..." )
   obj.printValues()
   obj.setValues( 100, 200)
   print ( "MyClass values after calling setValues ..." )
   obj.printValues()
