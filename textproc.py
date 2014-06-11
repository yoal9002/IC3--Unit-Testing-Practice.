# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import re

# Exceptions

class TextProcError(Exception):
    """
    Base Class for TextProc Excpetions

    """

    def __init__(self, msg):
        """
        TextProcError Constructor

        :param msg: error message

        """

        super().__init__(msg)

# Public Classes

class Processor:
    """
    Class for Processing Strings

    """

    def __init__(self, text):
        """
        Test Processor Constructor

        :param text: text string to process

        """

        if type(text) is not str:
            raise TextProcError("Processors require strings")

        self.text = text

    def __len__(self):
        return len(self.text)

    def count(self):
        return len(self)

    def count_alpha(self):
        alpha = re.compile(r'[a-z]')
        return len(alpha.findall(self.text))

    def count_numeric(self):
        alpha = re.compile(r'[1-9]')
        return len(alpha.findall(self.text))

    def count_vowels(self):
        vowels = re.compile(r'[aeou]', re.IGNORECASE)
        return len(vowels.findall(self.text))

    def is_phonenumber(self):
        phonenum = re.compile(r'^[1-9]{3}([\-.])*[1-9]{3}\1*[1-9]{3}$')
        if phonenum.match(self.text) is None:
            return False
        else:
            return True
