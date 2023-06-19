import math
import os
from random import randint

def Solve(a,b,c):
    if b > c:
        b,c = c,b
    lcm = b*c//math.gcd(b,c)
    full_part = a//lcm
    ans = full_part*b - 1
    a -= full_part*lcm
    ans += min(a+1,b)
    return ans

for test_index in range(40):
    if os.path.isdir("./TEST"+str(test_index)) == False:
        os.mkdir("./TEST"+str(test_index))
    inp = open("./TEST"+str(test_index)+"/MODULO.INP", "w")
    out = open("./TEST"+str(test_index)+"/MODULO.OUT", "w")
    q = 0
    inp_data = []
    out_data = []
    if test_index < 8:
        q = randint(1,10**5)
        if test_index % 4 == 3:
            q = 10**5
        for i in range(q):
            a,b,c = 0,0,0
            if test_index < 4:
                a = randint(1,10**4)
                b = randint(1,10**4)
            else:
                a = randint(1,10**9)
                b = randint(1,10**9)
            c = randint(1,10**9)
            if randint(1,3) == 1:
                c = randint(1,min(b,c))
            inp_data.append(["1",str(a),str(b),str(c)])
            out_data.append((a*b)%c)
    elif test_index < 16:
        q = randint(1,10**3)
        if test_index % 4 == 3:
            q = 10**3
        for i in range(q):
            a,b,c = 0,0,0
            b = randint(1,10**2)
            c = randint(1,10**2)
            if randint(1,20) == 20:
                c = b
            while max(b,c) > a:
                a = randint(1,10**4)
            inp_data.append(["2",str(a),str(b),str(c)])
            out_data.append(Solve(a,b,c))
    elif test_index < 24:
        q = randint(1,10**5)
        if test_index % 4 == 3:
            q = 10**5
        for i in range(q):
            a,b,c = 0,0,0
            select = randint(1,2)
            b = randint(1,10**5)
            c = randint(1,10**5)
            while max(b,c) > a:
                a = randint(1,10**9)
            inp_data.append([str(select),str(a),str(b),str(c)])
            if select == 1:
                out_data.append((a*b)%c)
            else:
                out_data.append(Solve(a,b,c))
    else:
        q = randint(1,10**5)
        if test_index % 4 == 3:
            q = 10**5
        for i in range(q):
            a,b,c = 0,0,0
            select = randint(1,2)
            b = randint(1,10**12)
            c = randint(1,10**12)
            while max(b,c) > a:
                a = randint(1,10**18)
            inp_data.append([str(select),str(a),str(b),str(c)])
            if select == 1:
                out_data.append((a*b)%c)
            else:
                out_data.append(Solve(a,b,c))
    inp.write(str(q)+"\n")
    for i in range(q):
        in_data = ""
        for j in inp_data[i]:
            in_data += j
            in_data += " "
        inp.write(in_data+"\n")
        out.write(str(out_data[i])+"\n")
    print("Test " + str(test_index) + " has completed.")
    inp.close()
    out.close()
        
