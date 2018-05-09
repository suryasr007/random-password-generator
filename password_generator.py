# -*-coding: utf-8 -*-

"""
Author          : Surya Teja <suryateja1919@gmail.com>
Description     : Random Password Generator
Website         : https://suryasr007.github.io
"""

import string
import random


class PasswordGenerator():
    """

    We can set properties such as

    | minlen     |   Minimum length of the password | 6
    | maxlen     |   Maximum length of the password | 16
    | minuchars  |   Minimum upper case characters required in password | 1
    | minlchars  |   Minimum lower case characters required in password | 1
    | minnumbers |   Minimum numbers required in password               | 1
    | minschars  |   Minimum special characters in the password         | 1

    Methods implemented in this class are

    generate() : Generates a password using default or custom propertiesself.

    shuffle_password(password, length) : Shuffle the given charactes and return a password from given characters.

    non_duplicate_password(length) : Generate a non duplicate key of givrn length

    """

    def __init__(self):
        self.minlen = 6
        self.maxlen = 16
        self.minuchars = 1
        self.minlchars = 1
        self.minnumbers = 1
        self.minschars = 1

        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.numbers_list = string.digits
        self._schars = ['!','#','$','%', '^', '&', '*', '(', ')', ',', '.', '-', '_', '+', '=', '<', '>', '?']
        self._allchars = list(self.lower_chars) + list(self.upper_chars) + list(self.numbers_list) + list(self._schars)


    def generate(self):
        """Generates a password using default or custom properties"""
        if self.minlen < 0 or self.maxlen < 0 or self.minuchars < 0 or self.minlchars < 0 or  self.minnumbers < 0 or self.minschars < 0 :
            raise ValueError("Character length should not be negative")

        if self.minlen > self.maxlen:
            raise ValueError("Minimum length cannot be greater than maximum length")

        collectiveMinLength = self.minuchars + self.minlchars + self.minnumbers + self.minschars

        if collectiveMinLength > self.minlen:
            self.minlen = collectiveMinLength

        final_pass = [random.choice(self.lower_chars) for i in range(self.minlchars)]
        final_pass += [random.choice(self.upper_chars) for i in range(self.minuchars)]
        final_pass += [random.choice(self.numbers_list) for i in range(self.minnumbers)]
        final_pass += [random.choice(self._schars) for i in range(self.minschars)]

        currentpasslen = len(final_pass)

        if len(final_pass) < self.maxlen:
            randlen = random.randint(self.minlen, self.maxlen)
            final_pass += [random.choice(self._allchars) for i in range(randlen-currentpasslen)]

        random.shuffle(final_pass)
        return ''.join(final_pass)


    def shuffle_password(self, password, maxlen):
        """Shuffle the given charactes and return a password from given characters."""
        final_pass = [random.choice(list(password)) for i in range(int(maxlen))]
        random.shuffle(final_pass)
        return ''.join(final_pass)


    def non_duplicate_password(self, maxlen):
        """Generate a non duplicate key of givrn length"""
        final_pass = []
        try:
            for i in range(maxlen):
                character = random.choice(self._allchars)
                element_index = self._allchars.index(character)
                final_pass.append(character)
                self._allchars.pop(element_index)
        except IndexError as ie:
            raise ValueError('Length should less than 77 characters.')
        random.shuffle(final_pass)
        return ''.join(final_pass)
