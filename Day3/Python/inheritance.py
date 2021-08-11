#!/usr/bin/python3

class Parent:

    def __init__(self):
        print ("Parent constructor ...")
        self.x = 10
        self.y = 20

    def parentPublicFunction(self):
        print ( "Parent Public Function ...")
        print ( self.x )
        print ( self.y )

    def _parentProtectedFunction(self):
        print ( "Parent Protected Function ...")

    def __parentPrivateFunction(self):
        print ( "Parent Private Function ...")

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)
        self.z = 30

    def childFunction(self):
        print ( "ChildFunction" )
        Parent.parentPublicFunction(self)
        print ( self.z )


if __name__ == "__main__":

   child = Child()
   child.childFunction()

   child._parentProtectedFunction()
   child.__parentPrivateFunction() 
