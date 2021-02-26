import sys

a, b = int(sys.argv[1]), int(sys.argv[2])

r = a % b

while r > 0 :
    a = b
    b = r
    r = a % b

print(str(b))
