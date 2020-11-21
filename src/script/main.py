from ball import *
from table import *
import os
## Main Procedure


## Set initial position
pos_x = 1.0
pos_y = 0.7
B = Ball()
B.initPos(pos_x,pos_y,Rb)

# Set Hit position
phi = np.pi*1.2
a = 0.0
b = 0.0
V = 5
theta = 0
B.hitBall(phi,a,b,V,theta)

## Set Table
T_name = "Table_O1"
TB = np.load("../data/"+T_name+".npy")

## Create logger
log_dir = "../log/Log_X{}_Y{}_p{}_a{}_b{}_V{}_t{}/".format(pos_x,pos_y,round(phi,2),a,b,V,round(theta,2))
if not(os.path.isdir(log_dir)):
        os.mkdir(log_dir)
log_f = open(log_dir+T_name+"_log.txt","w")


## Start Simulation
T_limit = 10; #Time limit in sec
OUT=0
step_cnt=0
while B.isStop():
    step_cnt+=1
    if step_cnt*dt >= T_limit:
       break; 
    try:
        B.printLog(log_f)
        OUT+=print_table(TB,B)
        B.proceed()
    except IndexError:
        break
cs=plt.imshow(OUT)


plt.savefig(log_dir+T_name+"_log.png")

log_f.close()
print("program terminated.")

