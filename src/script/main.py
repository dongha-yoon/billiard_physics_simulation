from ball import *
from table import *
import os
## Main Procedure

def do_simulation(phi,V):
    ## Set initial position
    pos_x = LX/2
    pos_y = LY/2
    B = Ball()
    B.initPos(pos_x,pos_y,Rb)

    # Set Hit position
    # phi = float(input())
    # V = float(input())
    a = 0.0
    b = 0.0
    theta = 0
    B.hitBall(phi,a,b,V,theta)

    ## Select Table
    T_name = "Formal_Table" #"Table_O1"
    TB = np.load("../data/"+T_name+".npy")

    ## Create logger
    log_dir = "../log/Log_X{}_Y{}_p{}_a{}_b{}_V{}_t{}/".format(pos_x,pos_y,round(phi,2),a,b,V,round(theta,2))
    if not(os.path.isdir(log_dir)):
            os.mkdir(log_dir)
    log_f = open(log_dir+T_name+"_log.txt","w")

    ## Start Simulation
    T_limit = 3; #Time limit in sec
    OUT=0
    step_cnt=0
    state = False
    while not B.isStop():
        # step_cnt+=1
        # if step_cnt*dt >= T_limit:
        #     print("Time Out")
        try:
            # B.printLog(log_f)
            OUT += print_table(TB,B)
            B.proceed()
            if not state:
                state = B.detect_collision(TB)
            else:
                state = True
        except IndexError:
            print("Exception: Out of Range")
            break

    cs=plt.imshow(OUT);plt.draw()
    plt.savefig(log_dir+T_name+"_log.png")
    log_f.write("# of collision:"+B.collision_count)
    log_f.close()
    return B.collision_count

print("program terminated.")

