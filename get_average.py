import matplotlib.pyplot as plt
import ast
import math


colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "cyan",
    "magenta",
    "yellow",
    "brown",
    "black"
]


x_keys = ["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10"]
x_sets = {"x1":[],"x2":[],"x3":[],"x4":[],"x5":[],"x6":[],"x7":[],"x8":[],"x9":[],"x10":[]}

y_set = []


i = 1
with open("bounded_all_coef_10.txt") as coef:
    for line in coef:
        real = ast.literal_eval(line)
        y_set.append(int(i))
        run = 1
        for key in x_keys:
            if x_sets[key]:
                new_value = (x_sets[key][-1]*(i-1)+real[run])/i
                x_sets[key].append(new_value)
                if key == "x1":
                    print(new_value)
            else:
                x_sets[key].append(real[run])
            run += 1
        i += 1

with open("bounded_all_avg_10.txt","w") as avg:
    for key in x_keys:
        avg.write(str(x_sets[key])+"\n")

p = 0 
for key in x_keys:
    plt.plot(y_set,x_sets[key],color = colors[p])
    p += 1
plt.show()

