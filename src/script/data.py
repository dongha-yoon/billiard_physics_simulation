import numpy as np

#Define constants and properties
#All of unit follows the MKS

#coefficient of restitution
e = 0.95

#friction coefficient
fs = 0.2        #coef of sliding
fr = 0.016      #coef of rolling
fsp= 0.044      #coef of spinning

#gravitational acceleration
G = 9.81

#Size of Table
LX = 2.845
LY = 1.422

#Cue Property
Mc = 0.600      #Mass

#Ball Properties.
Rb = 0.0655/2       #Radius
Mb = 0.250          #Mass
Ib = 2.0/5*Mb*Rb**2 #Moment of Inertia

#time
tc = 200e-6 #Collision time
dt = 0.005    #Time difference

