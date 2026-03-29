import ast
import math



with open("average_primes.txt") as avg:
    with open("graph_bounded_10.txt","w") as gr:
        for line in avg:
            new_set = []
            data_set = ast.literal_eval(line)
            step = math.floor(len(data_set)/100)
            print(step)
            for i in range(0,100):
                new_set.append(data_set[i*step])
            
            #gr.write(str(new_set)+"\n")