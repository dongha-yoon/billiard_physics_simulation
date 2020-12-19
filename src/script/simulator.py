from main import *

v = np.arange(0,100)
phi = np.arange(0,2*np.pi,0.1)

res = []

for vi in v:
    for pi in phi:
        do_simulation(pi,vi)