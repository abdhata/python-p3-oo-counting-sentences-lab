#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value=""):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if (type(value) is str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        if (self.value.endswith(".")):
            return True
        else:
            return False

    def is_question(self):
        if (self.value.endswith("?")):
            return True
        else:
            return False

    def is_exclamation(self):
        if (self.value.endswith("!")):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        return len([s for s in sentences if s.strip()])