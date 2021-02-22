from submissions.control_submission import get_c_side
import sys

a = sys.argv[1]
b = sys.argv[2]

print(get_c_side(int(a), int(b)))
