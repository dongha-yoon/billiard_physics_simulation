
import numpy as np

#######################################
#      Start Presets
#######################################

#Define constants.
#All of unit follows MKS


#Size of Table
LX = 2.845; LY = 1.422
scale_factor = 10000;
TX = np.arange(0,LX*scale_factor,1)
TY = np.arange(0,LY*scale_factor,1)
TX,TY = np.meshgrid(TX,TY)

#friction coefficient
fs = 0.2        #coef of sliding
fr = 0.016      #coef of rolling
fsp= 0.044      #coef of spinning

#Cue
Mc = 0.600      #Mass

#Ball
Rb = 0.0655/2       #Radius
Mb = 0.250          #Mass
Ib = 2.0/5*Mb*Rb**2 #Moment of Inertia

#collision time
tc = 200e-6

#Define Billiard ball object
class Ball:
    pos = np.array([0.0,0.0,0.0])
    vel = np.array([0.0,0.0,0.0])
    ang = np.array([0.0,0.0,0.0])
    def printInfo(self):
        print(self.pos);print(self.vel);print(self.ang)

    def initPos(self,px,py,pz):
        self.pos[0]=px; self.pos[1]=py; self.pos[2]=pz

    def hitBall(self,phi,a,b,V0,theta):
        F     = Mc*V0/tc*np.array([0,np.cos(theta),-np.sin(theta)])
        Fconv = np.array([F[1]*np.sin(phi),-F[1]*np.cos(phi),F[2]])
        if Fconv[2]<0:
            Fconv[2]=0
        self.vel   = tc/Mb*Fconv

        r     = np.array([-a,-np.sqrt(Rb**2-a**2-b**2),b])
        T     = np.cross(r,F)
        Tconv = np.array([T[0]*np.cos(phi)+T[1]*np.sin(phi),T[0]*np.sin(phi)-T[1]*np.cos(phi),T[2]])
        self.ang   = tc/Ib*Tconv

#######################################
#      End Presets
#######################################



#######################################
#      Start Main
#######################################


#Set Filed



#Set initial position in meter
pos_x = 1.2
pos_y = 0.7
B = Ball()
B.initPos(pos_x,pos_y,Rb)

#Set Hit position
phi = np.pi/3
a = 0.01
b = 0.01
V0 = 1
theta = np.pi/10
B.hitBall(phi,a,b,V0,theta)

B.printInfo()