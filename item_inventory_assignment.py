import numpy as np
import random

T = 1000
x_max = 10
# P(D=1) distribution
Pd = [i/1000 for i in range(T + 1)]
# holding cost
h = 0.01
# purchase cost
c = 10
# selling price
p = 20
# order cost
K = 10

V = np.array([[float(0) for i in range(T + 1)] for j in range(x_max + 1)])
alpha = np.array([[float(0)for i in range(T + 1)] for j in range(x_max + 1)])

# initialized the last column: hx
V[:, -1] = [x * h for x in range(0, x_max + 1)] 


for t in range(T - 1, 0, -1):
    if t > 900:
        c = 0
    elif t > 500 and t <= 900:
        c = 15
    else: 
        c = 10

    dIsOne = Pd[t]
    dIsZero = round(1 - dIsOne, 3)
    # P(d=1) increases linearly as t increases
    d = random.choices([1, 0], weights=(dIsOne, dIsZero), k = 1)[0]
    
    if t > 900:
        # At t > 900 no order can be placed, so the optimal policy would be just a copy of optimal policy at t = 900
        for x in range(0, x_max):
            Q = {}
            E = dIsOne * V[x - 1][t + 1] + dIsZero * V[x - 0][t + 1]  
            
            # items can only be sold
            V[x][t] = (-h * x)  + dIsOne * p + E

            # optimal policy remains unchanged after t = 900
            alpha[x][t]= alpha[x][t+1]

    # when  t <= 900
    else: 
        for x in range(0, x_max):
            Q = {}
            for a in range(max(d-x,0) , x_max - x + d):
                E = dIsOne * V[x - 1 + a][t + 1] + dIsZero * V[x - 0 + a][t + 1]
                order_cost = K if a > 0 else 0    
                Q[a] = (-h * x) - order_cost - (c * a)  + dIsOne * p + E
            V[x][t] = Q[max(d-x, 0)]
            alpha[x][t]= max(d-x, 0)
            for a in range(max(d-x,0), x_max-x+d):
                if(Q[a] > V[x][t]):
                    alpha[x][t]=a
                    V[x][t] = Q[a]



for i in range(x_max + 1):
    for j in range(990, T + 1):
        print(V[i][j],end=' ')
    print() 
print ('-------------------')



print('------------')

for i in range(x_max + 1):
    for j in range(990, T + 1):
        print(alpha[i][j], end = ' ')
    print()

print('------------')

for i in range(x_max + 1):
    for j in range(0, 11):
        print(V[i][j],end=' ')
    print() 

print('------------')

for i in range(x_max + 1):
    for j in range(0, 11):
        print(alpha[i][j], end = ' ')
    print()


'''
Choose appropriate X and A  use dynamic programming (programmed in 
python) to determine the total expected profit and the optimal order policy, 
starting with 0 inventory at time 0

- X(state) is  the current number of items in inventory max value of which can be
     x_max(currently 10 is used for simplicity of understanding) - current level + demand
- A(action) is placing an order 



'''