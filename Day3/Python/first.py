#!/usr/bin/python3

from second import F2

def F1():
    print ( "Inside F1 function from first.py ..." )
    F2()

if __name__ == "__main__":
  F1()
