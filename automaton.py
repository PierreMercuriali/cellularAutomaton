import sys, random
import matplotlib.pyplot as plt
length  = 100
steps   = 200
line    = []
for i in range(length):
    line.append(random.choice([0,1]))
rule = {"000": 0,
        "001": 1,
        "010": 1,
        "011": 1,
        "100": 0,
        "101": 1,
        "110": 1,
        "111": 0
        }        
def update(l):
    new = []
    for i in range(length):
        voisinage = str(l[(i-1)%length])+str(l[(i)%length])+str(l[(i+1)%length])
        new.append(rule[voisinage])
    return new

def weights(l):
    res = []
    for i in range(len(l)):
        res.append(l[i]*i)
    return res

for i in range(steps):
    plt.plot([i]*length, weights(line), ".", color=(float(i)/steps, 0, 0))
    line = update(line)    
    
plt.title("Rule 110")
plt.grid(True)
plt.show()
