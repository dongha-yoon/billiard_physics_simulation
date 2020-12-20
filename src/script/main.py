from ball import *
from table import *
import os
## Main Procedure

def do_simulation(phi,V,T_name):
    Error_NO = 0
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
    TB = np.load("../data/"+T_name+".npy")

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
            isCollide,angle = B.detect_collision(TB)
            if not state and isCollide:
                B.collide(angle)
                state = True
            elif not isCollide:
                state = False

        except IndexError:
            Error_NO = 1
            print("Exception: Out of Range, V:{},phi:{}".format(V,phi))
            break
        except ValueError:
            Error_NO = 2
            print("Exception: Value error, V:{},phi:{}".format(V,phi))
            return

    ## Create logger
    # log_dir = "../log/Log_X{}_Y{}_p{}_a{}_b{}_V{}_t{}/".format(pos_x,pos_y,round(phi,2),a,b,V,round(theta,2))
    log_dir = "../log/Log_p{}_V{}/".format(round(phi,2),V)
    if not(os.path.isdir(log_dir)):
            os.mkdir(log_dir)
    log_f = open(log_dir+T_name+"_log.txt","w")

    cs=plt.imshow(OUT);plt.draw()
    plt.savefig(log_dir+T_name+"_log.png");plt.clf()

    if Error_NO==1:
        log_f.write("\nException: IndexError")
        return 999999
    if Error_NO==2:
        log_f.write("\nException: ValueError")
        return 999999

    log_f.write("# of collision:"+str(B.collision_count))

    log_f.close()
    return B.collision_count


