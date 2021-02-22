from submissions.control import *

import os
from os.path import join, isfile, dirname

def tests(iterations):
    print("Test for: " + str(iterations))

    filePath = join(os.getcwd(), 'vysledok.txt')
    if isfile(filePath):
        os.remove(filePath)

    asterisk_triangles(iterations)

    if not isfile(filePath):
        fail("file not found")
    else:
        file = open(filePath)

        index = 1
        for line in file:
            if index > iterations:
                fail("more lines than it should be")
                return
            if get_test_line(index) != line:
                text ="[" + get_test_line(index) + "] does not match [" + line + "]"
                fail(text.encode())
                file.close()
                return
            index += 1
        if index <= iterations:
            fail("less than required amount of lines")
            return
        file.close()
        print("success")

def fail(text):
    print(text)
    print("FAIL")


def get_test_line(index):
    test_line = ''
    for i in range(0, index):
        test_line += "*"
    test_line += "\n"
    return test_line

if __name__ == "__main__":
    tests(10)
    tests(0)
    tests(3)