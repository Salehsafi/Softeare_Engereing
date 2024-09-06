class Number:
    def __init__(self, value):
        self.value = value

    def square(self):
        print("The square of the number is:", self.value ** 2)

class EvenNumber(Number):
    def __init__(self, value):
        super().__init__(value)
        if value % 2 != 0:
            raise ValueError("The value must be an even number")

    def square(self):
        print("The square of the even number is:", self.value ** 2)

import unittest

class TestNumber(unittest.TestCase):
    def test_number_square(self):
        number = Number(5)
        number.square()
        self.assertEqual(number.value, 5)

class TestEvenNumber(unittest.TestCase):
    def test_even_number_square(self):
        even_number = EvenNumber(4)
        even_number.square()
        self.assertEqual(even_number.value, 4)


# Added by Jungho Park 
class jungho:
    def addFive(self, x):
        return x+5

    def subtractFive(self, x):
        return x-5


class testAddFive(unittest.TestCase):
    def addFive(self):
        Jungho = jungho()
        self.assertEqual(Jungho.addFive(2), 7)
        self.assertEqual(Jungho.subtractFive(5), 0)

# Added by Atomu Maruyama
class atomu:
    def multiplyByTwo(self, x):
        return x*2
    
    def divideByTwo(self, x):
        return x/2
    
class testMultiplyByTwo(unittest.TestCase):
    def multiplyByTwo(self):
        Atomu = atomu()
        self.assertEqual(Atomu.multiplyByTwo(4), 8)
        self.assertEqual(Atomu.divideByTwo(12), 6)


if __name__ == "__main__":
    unittest.main()