import ast
avg = [0]
graph_avg = []
graph_x  = []

i = 0
with open("bounded_all_coef_1000.txt") as bc:
    for line in bc:
        real = ast.literal_eval(line)
        new_avg = (avg[-1]*len(avg)+real[1])/(len(avg)+1)
        avg.append(new_avg)
        if i%150 == 0:
            graph_x.append(real[0])
            graph_avg.append(new_avg)
            print("X")
        i+= 1
print(graph_x)
print("\n")
print(graph_avg)
