## Create and Set Table

from data import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# File_output_path = "/mnt/c/Users/aero5/Desktop/2020 Fall/Computaional_physics_project/src/data/"
Obstacle = Rb*10000 #The height of obstacles(+rails) are Rb

## Set grid

SF = 1000; #scale factor
size_x = int(LX*SF)
size_y = int(LY*SF)

tx = np.arange(0,size_x+1,1)
ty = np.arange(0,size_y+1,1)
TX,TY = np.meshgrid(tx,ty)

################
# Formal Table
################
Z = 0.0*TX*TY
Z[0,:] = Z[:,0] = Z[size_y,:] = Z[:,size_x] = Obstacle
# cs=plt.imshow(Z); plt.colorbar(cs); plt.show();plt.clf()
np.save("../data/Formal_Table",Z)

################
# Ellipse Table
################
Z = 0.0*TX*TY
a = size_x/2
b = size_y/2
for ix in range(0,int(size_x/2)):
    for iy in range(0,int(size_y/2)):
        if ix**2/a**2+iy**2/b**2 >= 1:
            Z[int(size_y/2)+iy,int(size_x/2)+ix] = Obstacle
            Z[int(size_y/2)+iy,int(size_x/2)-ix] = Obstacle
            Z[int(size_y/2)-iy,int(size_x/2)+ix] = Obstacle
            Z[int(size_y/2)-iy,int(size_x/2)-ix] = Obstacle
# plt.rcParams["figure.figsize"] = (30,20)
# cs=plt.imshow(Z); plt.colorbar(cs); plt.show();plt.clf()
np.save("../data/Ellipse_Table",Z)


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

