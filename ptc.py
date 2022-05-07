import math
import os
import random
import re
import sys

# Complete the 'appendAndDelete' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k

def appendAndDelete(s, t, k):
    # Write your code here
    c = 0
    sl = len(s)
    tl = len(t)
    while(c<=sl-1 and c<=tl-1 and s[c]==t[c]):
        c += 1
    if(k >= (sl+tl)):
        return "Yes"
    elif((k>= sl+tl-2*c) and (k-sl-tl+2*c)%2==0):
        return 'Yes'
    else:
        return 'No'
                      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    fptr.write(result + '\n')
    fptr.close()