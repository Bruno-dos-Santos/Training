# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

s = "\n".join([input() for x in range(n)])

for i in range(2):
    s = re.sub(" \&{2} ", " and ", s) 
    s = re.sub(" \|{2} ", " or ", s) 
print(s)
