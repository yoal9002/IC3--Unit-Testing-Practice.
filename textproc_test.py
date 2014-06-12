#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
    def test_isString(self):
        self.assertRaises(textproc.TextProcError, textproc.Processor, 123)

    def test_count(self):
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 62 ,"The count is correct" )

    def test_count_alpha(self):
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 52 ,"The count is correct" )
        
    def test_count_numeric(self):
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 10 ,"The count is correct" )
        
    def test_count_vowels(self):
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 10 ,"The count is correct" )
        
    def test_is_phonenumber(self):
        text = "720-400-4531"
        p = textproc.Processor(text)
        self.assertTrue(p.is_phonenumber())
    

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
