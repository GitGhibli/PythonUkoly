from submissions.control import *
from submissions.control import get_c_side as control_get_c_side

def tests():
    tests = [[3,4],[5,10],[7,4],[5,11],[6,4],[0,0],[100,100],[12,10],[13,4],[4,10],[7,4],[8,10],[3,1],[5,4],[3,112],[3,10],[25,4],[23,10],[22,4],[1,10]]

    for test in tests:
        if control_get_c_side(test[0], test[1]) != get_c_side(test[0], test[1]):
            print("fail for")
            print(test[0])
            print(test[1])
            return

    print("success")

if __name__ == "__main__":
    tests()