
import unittest
import numpy as np
from pytest import raises
from binsearch import binary_search

class MyTest(unittest.TestCase):
    
    def test_mymath(self):
        self.assertEqual(binary_search([2,3],2), 0)
        
    def test_char(self):
        with self.assertRaises(TypeError):
            binary_search(['a',3],2)
            
    def test_zerol(self):
        self.assertEqual(binary_search([],2), -1)
    
    def test_NaN(self):
        self.assertEqual(binary_search([2,np.NaN],2), 0)
        