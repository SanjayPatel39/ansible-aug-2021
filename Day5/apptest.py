#!/usr/bin/python3

import unittest
from app import sayHello

class Testing(unittest.TestCase):
    def test_sayHello(self):
        actualResponse   = sayHello() 
        expectedResponse = 'Hello World!'
        self.assertEqual(actualResponse, expectedResponse)
    
if __name__ == '__main__':
    unittest.main() 
