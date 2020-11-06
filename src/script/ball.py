from data import *

def getSize(vec):
    sq_sum = 0
    for i in vec:
        sq_sum+= i**2
    return np.sqrt(sq_sum)


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
    def proceed(self):
        self.pos = self.pos+self.vel*dt

        direction = self.vel/getSize(self.vel)
        rel_vel = self.vel + np.cross(Rb*np.array([0,0,1]),self.ang) #Compute relative velocity between Center-Floor
        if getSize(rel_vel)==0:#rolling
            print("rolling!")
            self.vel = self.vel - fr*G*dt
            temp= self.ang[2];self.ang[2]=0
            self.ang = self.ang/getSize(self.ang) * getSize(self.vel)/Rb
            self.ang[2] = temp
        else :#sliding
            self.vel = self.vel - fs*G*dt
            self.ang = self.ang - np.cross(np.array([0,0,1]),direction)*5*fs*G/(2*Rb)*dt

        self.ang[2] = self.ang[2] - 5*fsp*G/(2*Rb)*dt


    def isStop(self):
        return (self.vel[0]+self.vel[1]+self.vel[2])

