import sys
from os import listdir, system, remove
from os.path import isfile, isdir, join, dirname

ASSIGNMENTS = "assignments"
SUBMISSIONS = "submissions"
TEST_FILE = "test.py"

assignment_from_cmd = None

if len(sys.argv) > 1:
    assignment_from_cmd = sys.argv[1]

def test_all():
    assignment = ""

    if assignment_from_cmd is None:
        assignment = input("assignment name: ")
    else:
        assignment = assignment_from_cmd

    assignment_path = join(dirname(__file__), ASSIGNMENTS, assignment)
    submissions_path = join(assignment_path, SUBMISSIONS)

    if not isdir(assignment_path):
        print("invalid directory")
        print(assignment_path)
        return

    submissions = [f for f in listdir(submissions_path) if isfile(join(submissions_path, f))]

    for submission in submissions:
        submissionName = submission.replace(".py", "")
        print('=====================================================================')
        print('=====================================================================')
        print(submissionName)

        test_template = open(join(assignment_path, "test.py"), "r")
        test_file = open(join(assignment_path,submissionName + "_test.py"), "w")
        
        test_template.readline()
        test_file.write("from submissions." + submissionName + " import *\n")

        for line in test_template:
            test_file.write(line)

        test_file.close()
        test_template.close()
        
        test_path = ASSIGNMENTS + '/' + assignment + '/' + submissionName + "_test.py"
        system('cmd /c echo ' + assignment)
        system('cmd /c py ' + test_path)

        remove(test_path)


if __name__ == '__main__':
    test_all()