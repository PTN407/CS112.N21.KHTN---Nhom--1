import math
import random
import os
int_limit = 2147483647
i64_limit = 9223372036854775807
for test_index in range(20):
    if os.path.isdir("./TEST"+str(test_index)) == False:
        os.mkdir("./TEST"+str(test_index))
    inp = open("./TEST"+str(test_index)+"/GIAITRI.INP", "w")
    out = open("./TEST"+str(test_index)+"/GIAITRI.OUT", "w")
    t = random.randint(1,200)
    if test_index % 5 == 4:
        t = 200
    inp.write(str(t)+"\n")
    for i in range(t):
        a,b = -1,-1
        ans = 10**99
        if test_index < 5:
            while ans >= int_limit:
                a = random.randint(1,31)
                b = random.randint(1,31)
                ans = a**b + b**a
        elif test_index < 10:
            while ans >= i64_limit:
                a = random.randint(1,63)
                b = random.randint(1,63)
                ans = a**b + b**a
        else:
            a = random.randint(1,1000)
            b = random.randint(1,1000)
            if test_index == 19:
                a = 1000-i
                b = 1000-i
            ans = a**b + b**a
        inp.write(str(a)+" "+str(b)+"\n")
        out.write(str(ans)+"\n")
    print("Test " + str(test_index) + " has completed.")
    inp.close()
    out.close()
        
