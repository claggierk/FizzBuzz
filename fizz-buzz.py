import unittest

def FizzBuzz(use_mod):
    increment_by_3 = 3
    increment_by_5 = 5

    multiple_of_3 = 3
    multiple_of_5 = 5

    output = []

    for i in range(1, 101, 1):
        if use_mod:
            mod3 = i % 3 == 0
            mod5 = i % 5 == 0
        else:
            # This solution does NOT use the mod operator
            mod3 = False
            if i == multiple_of_3:
                mod3 = True
                multiple_of_3 += increment_by_3

            mod5 = False

        if i == multiple_of_5:
            mod5 = True
            multiple_of_5 += increment_by_5

        result = ""
        if mod3 and mod5:
            result = 'FizzBuzz'
            output.append(result)
        elif mod3:
            result = 'Fizz'
            output.append(result)
        elif mod5:
            result = 'Buzz'
            output.append(result)
        else:
            result = i
            output.append(result)

    return output

class FizzBuzzTest(unittest.TestCase):
    def testModVsNoMod(self):
        mod_output = FizzBuzz(True)
        no_mod_output = FizzBuzz(False)
        self.assertEqual(mod_output, no_mod_output)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
