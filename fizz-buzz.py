import unittest

class FizzBuzz:
    def __init__(self, upper_bound, use_mod, fizz=3, buzz=5):
        self.fizz = fizz
        self.buzz = buzz
        self.upper_bound = upper_bound
        self.use_mod = use_mod

        self.fizz_buzz_output = []
        self.fizz_multiple = self.fizz
        self.buzz_multiple = self.buzz

    def use_modulo(self, number):
        """ Using modulo, determine whether a given number is:
        divisible by the fizz argument (3 by default)
        divisibly by the buzz argument (5 by default)
        """
        fizz_divisible = number % self.fizz == 0
        buzz_divisible = number % self.buzz == 0
        return fizz_divisible, buzz_divisible

    def no_modulo(self, number):
        """ Without using modulo, determine whether a given number is:
        divisible by the fizz argument (3 by default)
        divisibly by the buzz argument (5 by default)
        """
        fizz_divisible = False
        if number == self.fizz_multiple:
            fizz_divisible = True
            self.fizz_multiple += self.fizz

        buzz_divisible = False
        if number == self.buzz_multiple:
            buzz_divisible = True
            self.buzz_multiple += self.buzz

        return fizz_divisible, buzz_divisible

    def fizz_buzz(self):
        """ for every number from 1 to upper bound (inclusive):
        if divisible by the fizz argument (3 by default) and not the buzz argument (5 by default), print 'Fizz'
        if divisible by the buzz argument (5 by default) and not the fizz argument (3 by default), print 'Buzz'
        if divisible by BOTH the fizz AND buzz arguments, print 'FizzBuzz'
        otherwise print the number
        """
        for number in range(1, self.upper_bound+1, 1):
            if self.use_mod:
                fizz_divisible, buzz_divisible = self.use_modulo(number)
            else:
                fizz_divisible, buzz_divisible = self.no_modulo(number)

            result = str(number) # default the result to the iteration #
            if fizz_divisible and buzz_divisible:
                result = 'FizzBuzz'
            elif fizz_divisible:
                result = 'Fizz'
            elif buzz_divisible:
                result = 'Buzz'

            # instead of printing, adding to a list
            self.fizz_buzz_output.append(result)

class FizzBuzzTest(unittest.TestCase):
    def testModVsNoMod(self):
        mod = FizzBuzz(100, True)
        mod.fizz_buzz()
        no_mod = FizzBuzz(100,  False)
        no_mod.fizz_buzz()

        # string comparison is probably expensive...
        self.assertEqual("\n".join(mod.fizz_buzz_output), "\n".join(no_mod.fizz_buzz_output))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
