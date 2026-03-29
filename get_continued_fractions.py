import math


def get_coefficients(x):
    coefficients = []
    N = x
    m = 0
    d = 1
    a_0 = math.floor(math.sqrt(N))
    while True:
        a = math.floor((math.sqrt(N)+m)/d)
        b = math.floor((a_0+m)/d)
        coefficients.append(a)
        if a-b != 0:
            print("problem")
        m = a*d - m
        d = (N-m**2)/d
        if 2*coefficients[0] == coefficients[-1]:
            return (coefficients)
        

def ratio_of_coefficients(x,digit):
    total = 0
    x_coefficients = get_coefficients(x)
    for number in x_coefficients[1:]:
        if number == digit:
            total+=1
    partion = total/(len(x_coefficients)-1)
    return partion

"""with open("continued_fractions_new.txt","w") as cf:
    for i in range(1,10**6):
        check = math.sqrt(i)
        if check.is_integer()==False:
            coefficients = get_coefficients(i)
            coefficients.insert(0,i)
            cf.write(str(coefficients)+"\n")
            if i%10000==0:
                print(i)"""

print(get_coefficients(2343))