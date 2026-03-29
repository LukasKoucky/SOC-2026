import ast 
import math
import linecache

avg= 0
total = 0
run = 0
con_avg = []
bound = 10

with open("coefficient_primes.txt") as cf:
    with open("bounded_p_10.txt","w") as odp:
        for line in cf:
            info = ast.literal_eval(line)
            if (len(info)-2)>bound:
                odp.write(str(info)+"\n")
                print(info[0])
            if info[0]>1000000:
                break

                




"""with open("odp.txt") as odp:
        for line in odp:
            new_set = []
            x_val = []
            data_set = ast.literal_eval(line)
            step = math.floor(len(data_set)/100)
            print(step)
            for i in range(0,100):
                new_set.append(data_set[i*step])
            for i in range(0,100):
                  x_val.append(step*i)
            print(x_val)"""

                
