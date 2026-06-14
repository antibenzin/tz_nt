import math
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'r', encoding='utf-8') as f:
    coordinates = f.read().split()

xc, yc, xr, yr = [float(item) for item in coordinates]

with open(file2, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue

        px, py = map(float, line.split())
        value = ((px - xc) ** 2) / (xr ** 2) + ((py - yc) ** 2) / (yr ** 2)

        if value < 1:
                status = 1
        elif math.isclose(value, 1.0, rel_tol=1e-9):
                status = 0
        else:
                status = 2
        
        print(status)