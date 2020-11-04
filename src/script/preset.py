import numpy as np

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
Rb = 0.0655/2     #Radius
Mb = 0.250        #Mass
Ib = 2/5*Mb*Rb**2 #Moment of Inertia

#collision time
tc = 200e-6

#Define Billiard ball object
class Ball:
    pos = [0.0,0.0,0.0]
    vel = [0.0,0.0,0.0]
    ang = [0.0,0.0,0.0]
    def init(px,py,pz):
        pos = [px,py,pz]
    def hitBall(phi,a,b,V0,theta):
        F     = Mc*V0/tc*[0,np.cos(theta),-np.sin(theta)]
        Fconv = [F[1]*np.sin(phi),-F[1]*np.cos(phi),F[2]]
        if Fconv[2]<0:
            Fconv=0
        vel   = tc/Mb*Fconv

        r     = [-a,-np.sqrt(Rb**2-a**2-b**2),b]
        T     = np.cross(r,F)
        Tconv = [T[0]*np.cos(phi)+T[1]*np.sin(phi),T[0]*np.sin(phi)-T[1]*np.cos(phi),T[2]]
        ang   = tc/Ib*Tconv
    