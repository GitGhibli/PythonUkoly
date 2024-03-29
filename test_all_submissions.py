import sys
from os import listdir, remove
from os.path import isfile, isdir, join, dirname

import subprocess

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
        immediate_print("invalid directory")
        immediate_print(assignment_path)
        return

    submissions = [f for f in listdir(submissions_path) if isfile(join(submissions_path, f))]
    
    immediate_print(assignment)
    
    for submission in submissions:
        submissionName = submission.replace(".py", "")
        immediate_print('=====================================================================')
        immediate_print('=====================================================================')
        immediate_print(submissionName)

        test_template = open(join(assignment_path, "test.py"), "r")
        test_file = open(join(assignment_path,submissionName + "_test.py"), "w")
        
        test_template.readline()
        test_file.write("from submissions." + submissionName + " import *\n")

        for line in test_template:
            test_file.write(line)

        test_file.close()
        test_template.close()
        
        test_path = ASSIGNMENTS + '/' + assignment + '/' + submissionName + "_test.py"
        try:
            output = subprocess.check_output(["python", test_path], stderr=subprocess.STDOUT, timeout=2)
            immediate_print(output.decode().replace('\r', ''))
        except subprocess.TimeoutExpired as e:
            immediate_print("code timeouted")    
            print("FAIL")
        except subprocess.CalledProcessError as e:
            immediate_print(e.output.decode().replace('\r', ''))
            print("FAIL")
            
        remove(test_path)
    
    print("DONE")

# We use immediate print because when child processes end they write first, but we want to preserve order of messages
def immediate_print(text):
    print(text, flush=True)

if __name__ == '__main__':
    test_all()