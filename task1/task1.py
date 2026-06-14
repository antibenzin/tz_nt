import sys

n1, m1, n2, m2 = map(int, sys.argv[1:])

path1 = [1] 
path2 = [1] 
curr_1 = 1 + (m1 - 1) % n1
curr_2 = 1 + (m2 - 1) % n2

while curr_1 != 1 or curr_2 != 1:
        if curr_1 != 1:
            path1.append(curr_1)
            curr_1 = 1 + (curr_1 + m1 - 2) % n1
        if curr_2 != 1:
            path2.append(curr_2)
            curr_2 = 1 + (curr_2 + m2 - 2) % n2
  
print("".join(map(str, path1 + path2)))