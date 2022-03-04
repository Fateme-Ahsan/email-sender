#In the name of God
from numpy import random
for i in range(1, 101):
    file1 = open("in/input" + str(i) + ".txt", "w")
    n = 20 - random.randint(20 - 1)
    k = 10 - random.randint(9)
    file1.write(str(n) + " " + str(k))
    for j in range(k):
        x = n - random.randint(n - 1)
        y = n - random.randint(n - 1)
        file1.write("\n" + str(x) + " " + str(y))
