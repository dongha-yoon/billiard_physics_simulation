## Create and Set Table

from data import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# File_output_path = "/mnt/c/Users/aero5/Desktop/2020 Fall/Computaional_physics_project/src/data/"
Obstacle = Rb*1000 #The height of obstacles(+rails) are Rb

## Set grid

SF = 1000; #scale factor
size_x = int(LX*SF)
size_y = int(LY*SF)

tx = np.arange(0,size_x+1,1)
ty = np.arange(0,size_y+1,1)
TX,TY = np.meshgrid(tx,ty)

set_flag = 0
if set_flag:
    ################
    # Formal Table
    ################
    padd=30
    Z = 0.0*TX*TY
    Z[0:padd,:] = Z[:,0:padd] = Z[size_y-padd:,:] = Z[:,size_x-padd:] = Obstacle
    np.save("../data/Formal_Table",Z)

    ################
    # Ellipse Table
    ################
    padd=30
    Z = 0.0*TX*TY
    a = size_x/2-padd
    b = size_y/2-padd
    for ix in range(0,int(size_x/2)):
        for iy in range(0,int(size_y/2)):
            if ix**2/a**2+iy**2/b**2 >= 1:
                Z[int(size_y/2)+iy,int(size_x/2)+ix] = Obstacle
                Z[int(size_y/2)+iy,int(size_x/2)-ix] = Obstacle
                Z[int(size_y/2)-iy,int(size_x/2)+ix] = Obstacle
                Z[int(size_y/2)-iy,int(size_x/2)-ix] = Obstacle
    np.save("../data/Ellipse_Table",Z)
    

    ################
    # Table With Obstacles 1
    ################
    padd=30
    Z = 0.0*TX*TY
    Z[0:padd,:] = Z[:,0:padd] = Z[size_y-padd:,:] = Z[:,size_x-padd:] = Obstacle
    # Z[int(size_x*0.5):int(size_x*0.6),int(size_y*0.3):int(size_y*0.4)] = Obstacle
    Z[1000:1300,1000:1200] = Obstacle
    for ix in range(0,int(size_x/2)):
        for iy in range(0,int(size_y/2)):
            if ix**2+iy**2 <= 2000:
                Z[int(size_y/2)+iy,int(size_x/2)+ix] = Obstacle
                Z[int(size_y/2)+iy,int(size_x/2)-ix] = Obstacle
                Z[int(size_y/2)-iy,int(size_x/2)+ix] = Obstacle
                Z[int(size_y/2)-iy,int(size_x/2)-ix] = Obstacle
    np.save("../data/Table_O1",Z)

    ################
    # Table With Obstacles 2
    ################
    padd=30
    Z = 0.0*TX*TY
    Z[0:padd,:] = Z[:,0:padd] = Z[size_y-padd:,:] = Z[:,size_x-padd:] = Obstacle
    
    Z[int(0.25*size_y):int(0.45*size_y),int(size_x/2-padd):int(size_x/2+padd)] = Obstacle
    Z[int(0.55*size_y):int(0.75*size_y),int(size_x/2-padd):int(size_x/2+padd)] = Obstacle
    Z[int(0.45*size_y):int(0.55*size_y),int(size_x/4-padd):int(size_x/4+padd)] = Obstacle
    Z[int(0.45*size_y):int(0.55*size_y),int(size_x/4*3-padd):int(size_x/4*3+padd)] = Obstacle
    np.save("../data/Table_O2",Z)    

    print("Table created!")


def print_table(TB,Obj):
    BE = 1000 #Ball existence
    ZB = 0*TB
    ZB[int(Obj.pos[1]*SF),int(Obj.pos[0]*SF)] = BE
    for ix in range(0,int(Rb*SF)):
        for iy in range(0,int(Rb*SF)):
            if ix**2+iy**2 < (Rb*SF)**2:
                ZB[int(Obj.pos[1]*SF)+iy,int(Obj.pos[0]*SF)+ix] = BE
                ZB[int(Obj.pos[1]*SF)+iy,int(Obj.pos[0]*SF)-ix] = BE
                ZB[int(Obj.pos[1]*SF)-iy,int(Obj.pos[0]*SF)+ix] = BE
                ZB[int(Obj.pos[1]*SF)-iy,int(Obj.pos[0]*SF)-ix] = BE
    # cs=plt.imshow(TB+ZB); plt.draw()
    return TB+ZB

