def fizzbuzz():
    increment_by_3 = 3
    increment_by_5 = 5

    multiple_of_3 = 3
    multiple_of_5 = 5

    for i in range(1, 101, 1):
        # Most intuitive solution
        # mod3 = i % 3 == 0
        # mod5 = i % 5 == 0

        # This solution does NOT use the mod operator
        mod3 = False
        if i == multiple_of_3:
            mod3 = True
            multiple_of_3 += increment_by_3

        mod5 = False
        if i == multiple_of_5:
            mod5 = True
            multiple_of_5 += increment_by_5

        if mod3 and mod5:
            print 'FizzBuzz'
        elif mod3:
            print 'Fizz'
        elif mod5:
            print 'Buzz'
        else:
            print i

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()
