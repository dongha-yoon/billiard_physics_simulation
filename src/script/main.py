from ball import *
from table import *

## Main Procedure


## Set initial position
pos_x = 1.2
pos_y = 0.7
B = Ball()
B.initPos(pos_x,pos_y,Rb)

# Set Hit position
phi = np.pi/2
a = 0.03
b = 0.0
V = 1
theta = np.pi/2.5
B.hitBall(phi,a,b,V,theta)

## Create logger
filename = "../log/Log_X{}_Y{}_p{}_a{}_b{}_V{}_t{}".format(pos_x,pos_y,round(phi,2),a,b,V,round(theta,2))
log_f = open(filename,"w")

## Set Table
# plt.rcParams["figure.figsize"] = (30,20)
TB = np.load("../data/Ellipse_Table.npy")

## Start Simulation
T_limit = 1; #Time limit in sec
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
plt.show()

print("program terminated.")

