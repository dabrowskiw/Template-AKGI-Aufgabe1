import math
import random
import string
from unittest import TestCase
import ast

import aufgaben


class AufgabenTest(TestCase):
    def count_method_lines(self, methodname):
        f = open("aufgaben.py", "r")
        t = ast.parse(f.read())
        lines = [f.end_lineno - f.lineno for f in t.body if type(f) == ast.FunctionDef and f.name == methodname][0]
        f.close()
        return lines

    def test_text_to_array_lines(self):
        self.assertEqual(self.count_method_lines("text_to_array"), 1, "Bitte in einer Zeile lösen!")

    def test_text_to_array_values(self):
        self.assertListEqual(aufgaben.text_to_array("test"), ['t', 'e', 's', 't'])

    def test_text_to_array_empty(self):
        self.assertListEqual(aufgaben.text_to_array(""), [])

    def test_count_needle_lines(self):
        self.assertEqual(self.count_method_lines("count_needle"), 1, "Bitte in einer Zeile lösen!")

    def test_count_needle_values(self):
        for trial in range(10):
            needle = random.choice(string.ascii_lowercase)
            haystack = "".join(random.choices(string.ascii_lowercase, k=random.randint(20,50)))
            self.assertEqual(aufgaben.count_needle(haystack, needle), haystack.count(needle), "Used needle: " +
                             needle + ", used haystack: " + haystack)

    def test_odd_numbers_lines(self):
        self.assertEqual(self.count_method_lines("odd_numbers"), 1, "Bitte in einer Zeile lösen!")

    def test_odd_numbers_values(self):
        for trial in range(10):
            maxvalue = random.randint(10,100)
            values = aufgaben.odd_numbers(maxvalue)
            self.assertEqual(len(values), math.floor(maxvalue/2))
            lastvalue = 0
            for value in values:
                self.assertTrue(value % 2 == 1)
                self.assertTrue(value > lastvalue)
                lastvalue = value

    def test_primes_lines(self):
        self.assertEqual(self.count_method_lines("primes"), 1, "Bitte in einer Zeile lösen!")

    def test_primes_values(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
        for trial in range(10):
            maxvalue = random.randint(1, 500)
            self.assertListEqual(aufgaben.primes(maxvalue), [x for x in primes if x < maxvalue])
