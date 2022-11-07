
T = 10
x_max = 10
d=2
h=1
K=5
V=[[0 for i in range(x_max+1)] for j in range(T+1)]

alpha = [[0 for i in range(x_max+1)] for j in range(T+1)]


for state in range (x_max+1):
    V[state][T] = h*state

for t in range(T-1, 1, -1):
    for x in range(0, x_max+1):

        Q = [0 for i in range(0 , x_max-x+d+1)]

        for a in range(max(d-x,0) , x_max-x+d+1):
            order_cost = K if a > 0 else 0
            Q[a] = x*h + order_cost + V[x-d+a][t+1]
        
        V[x][t] = Q[max(d-x, 0)]
        alpha[x][t]=max(d-x,0)
        # finding action corresponding to minimum of all values
        for a in range(max(d-x,0), x_max-x+d):
            if(Q[a] < V[x][t]):
                alpha[x][t]=a
                V[x][t] = Q[a]

for i in range(x_max + 1):
    for j in range(T+1):
        print(V[i][j],end=' ')
    print() 

print('------------')
for i in range(x_max + 1):
    for j in range(T+1):
        print(alpha[i][j],end=' ')
    print() 

