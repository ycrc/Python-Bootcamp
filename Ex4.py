
import math, random
import matplotlib.pyplot as plt

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def cost(curr):
    total=0
    n=len(curr)
    for i in range(n):
        total+=dist(curr[i], curr[(i+1)%n])
    return total

def initial(n):
    return [[random.randint(-1000,1000), random.randint(-1000,1000)] for i in range(n)]

def p_accept(candcost, currcost, T):
    p = math.exp(-abs(candcost - currcost) / T)
    return p

def doswap(curr):
    cand=curr[:]
    n=len(cand)
    i,j = sorted(random.sample(range(n),2))
    cand[i:j+1] = reversed(cand[i:j+1])
    return cand

def plot(path):
    xs = []; ys = []
    for x,y in path:
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, 'co-')
    plt.show()

def optimize(cities):
    curr=cities
    currcost=cost(curr)
    T=math.sqrt(len(cities))
    while T > 1e-10:
        cand=doswap(curr)
        candcost=cost(cand)
        if candcost<currcost: 
            curr=cand
            currcost=candcost
            print("forward T %f cost %f" % (T, currcost))
        elif p_accept(candcost, currcost, T) > random.random():
            curr=cand
            currcost=candcost
            print("backward T %f cost %f" % (T, currcost))
        T=T*.999
    return curr

if __name__=='__main__':
    cities=initial(100)
    print("cost {}".format(cost(cities)))
    plot(cities)
    best=optimize(cities)
    print("cost {}".format(cost(best)))
    plot(best)
