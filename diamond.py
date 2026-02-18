#Name : Faith Nyambura
# Date : 17/02/2026
# program to illustrate diamond in py

def print_diamond(rows):
    print(f"a diamond pattern of a given number of rows") (odd numbers work best for a perfect shape).
    # upper half of the diamond
    for i in range(rows):
        # print leading spaces
        for i in range(rows- i - 1):
            print(' ', end='')
            # print stars
            for k in range(2 * i + 1):
                print('*', end='')
                # move to the next line
                print()

                # lower half of the diamond (starts from the second-to-)
                for i in range(rows - 2, -1, -1):
                    # print leading spaces
                    for j in range(rows - i - 1):
                        print(' ', end='')
                        # print stars
                        for k in range(2 * i + 1):
                            print('*', end='')
                            # move to the next line
                            print()
                            # get user input for the 

