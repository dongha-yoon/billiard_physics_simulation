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
a = 0.0
b = 0.0
V = 1
theta = 0
B.hitBall(phi,a,b,V,theta)

## Create logger
filename = "../log/Log_{}{}{}{}{}{}{}".format(pos_x,pos_y,phi,a,b,V,theta)
log_f = open(filename,"w")

## Set Table
# plt.rcParams["figure.figsize"] = (30,20)
TB = np.load("../data/Ellipse_Table.npy")

## Start Simulation
OUT=0
print_flag=0
while B.isStop():
    try:
        B.printLog(log_f)
        OUT+=print_table(TB,B)
        B.proceed()
    # if B.pos[0]>LX or B.pos[1]>LY or B.pos[0]<0 or B.pos[1]<0 or TB[int(B.pos[1]*SF),int(B.pos[0]*SF)]==Obstacle:
    except IndexError:
        cs=plt.imshow(OUT)
        plt.show()
        print_flag=1
        break
   
if not print_flag:
    cs=plt.imshow(OUT)
    plt.show()

print("program terminated.")

