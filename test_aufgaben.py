import math
import random
import string
from unittest import TestCase
import ast
import inspect
import pytest

import aufgaben


class AufgabenTest(TestCase):
    @staticmethod
    def count_method_lines(methodname):
        f = open("aufgaben.py", "r")
        t = ast.parse(f.read())
        lines = [f.end_lineno - f.lineno for f in t.body if type(f) == ast.FunctionDef and f.name == methodname][0]
        f.close()
        return lines

    @pytest.mark.listcomprehensions
    def test_text_to_array_lines(self):
        self.assertEqual(self.count_method_lines("text_to_array"), 1, "Bitte in einer Zeile lösen!")

    @pytest.mark.listcomprehensions
    def test_text_to_array_values(self):
        self.assertListEqual(aufgaben.text_to_array("test"), ['t', 'e', 's', 't'])

    @pytest.mark.listcomprehensions
    def test_text_to_array_empty(self):
        self.assertListEqual(aufgaben.text_to_array(""), [])

    @pytest.mark.listcomprehensions
    def test_count_needle_lines(self):
        self.assertEqual(self.count_method_lines("count_needle"), 1, "Bitte in einer Zeile lösen!")

    @pytest.mark.listcomprehensions
    def test_count_needle_values(self):
        for trial in range(10):
            needle = random.choice(string.ascii_lowercase)
            haystack = "".join(random.choices(string.ascii_lowercase, k=random.randint(20,50)))
            self.assertEqual(aufgaben.count_needle(haystack, needle), haystack.count(needle), "Used needle: " +
                             needle + ", used haystack: " + haystack)

    @pytest.mark.listcomprehensions
    def test_odd_numbers_lines(self):
        self.assertEqual(self.count_method_lines("odd_numbers"), 1, "Bitte in einer Zeile lösen!")

    @pytest.mark.listcomprehensions
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

    @pytest.mark.listcomprehensions
    def test_primes_lines(self):
        self.assertEqual(self.count_method_lines("primes"), 1, "Bitte in einer Zeile lösen!")

    @pytest.mark.listcomprehensions
    def test_primes_values(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
        for trial in range(10):
            maxvalue = random.randint(1, 500)
            self.assertListEqual(aufgaben.primes(maxvalue), [x for x in primes if x < maxvalue])

    @pytest.mark.generators
    def test_odd_numbers_generator_isgenerator(self):
        self.assertTrue(inspect.isgenerator(aufgaben.odd_numbers_generator()), "Funktion soll ein Generator sein.")

    @pytest.mark.generators
    def test_odd_numbers_generator_values(self):
        lastvalue = -1
        for value in aufgaben.odd_numbers_generator():
            self.assertTrue(value % 2 == 1)
            self.assertEqual(2, value - lastvalue)
            lastvalue = value
            if lastvalue > 200:
                break

    @pytest.mark.generators
    def test_fibonacci_generator_isgenerator(self):
        self.assertTrue(inspect.isgenerator(aufgaben.fibonacci_generator()), "Funktion soll ein Generator sein.")

    @pytest.mark.generators
    def test_fibonacci_generator_values(self):
        fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
        pos = 0
        for value in aufgaben.fibonacci_generator():
            self.assertEqual(value, fib[pos])
            pos += 1
            if pos >= len(fib):
                break
