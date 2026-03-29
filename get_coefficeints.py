import math
import ast

def ratio_of_coefficients(x,digit):
    total = 0
    x_coefficients = x
    for number in x_coefficients:
        if number == digit:
            total+=1
    partion = total/(len(x_coefficients))
    return partion





with open("bounded_p_10.txt") as cf:
    with open("bounded_p_coef_10.txt","w") as coef:
        for line in cf:
            partions = []
            x = ast.literal_eval(line)
            partions.append(x[0])
            continued_fraction = x[2:]
            for i in range(1,11):
                partions.append(ratio_of_coefficients(continued_fraction,i))
            coef.write(str(partions)+"\n")
            if x[0]%10000==0:
                print(x[0])

