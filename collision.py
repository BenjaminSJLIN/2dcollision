import math

#data input
m1=int(input("m1:"))
m2=int(input("m2:"))

r1=int(input("r1:"))
r2=int(input("r2:"))

v1=input("v1:").split()
v2=input("v2:").split()
v1=[int(v1[0]),int(v1[1])]
v2=[int(v2[0]),int(v2[1])]

x01=input("x1:").split()
x02=input("x2:").split()
x01=[int(x01[0]),int(x01[1])]
x02=[int(x02[0]),int(x02[1])]

#==============================================================================
A=(v1[0]-v2[0])**2+(v1[1]-v2[1])**2
B=((x01[0]-x02[0])*(v1[0]-v2[0])+(x01[1]-x02[1])*(v1[1]-v2[1]))*2
C=(x01[0]-x02[0])**2+(x01[1]-x02[1])**2

a=A
b=B
c=C-(r1+r2)**2

if b**2-4*a*c<0 or a==0:
    print("no collision")
    collision=False
else:
    collision=True
    t=(-b-math.sqrt(b**2-4*a*c))/(2*a)#time of collision

    x1=x01[0]+v1[0]*t
    y1=x01[1]+v1[1]*t
    x2=x02[0]+v2[0]*t
    y2=x02[1]+v2[1]*t

    #line of centers
    l=[x1-x2,y1-y2]
    long_l=math.sqrt(l[0]**2+l[1]**2)
    l=[l[0]/long_l,l[1]/long_l]

    #Impulse
    J=(2*m1*m2)/(m1+m2)*((l[0]*v1[0]+l[1]*v1[1])-(l[0]*v2[0]+l[1]*v2[1]))
    vectorJ=[J*l[0],J*l[1]]

    #new velocities
    v_1=[v1[0]-vectorJ[0]/m1,v1[1]-vectorJ[1]/m1]
    v_2=[v2[0]+vectorJ[0]/m2,v2[1]+vectorJ[1]/m2]

def x(time):
    if collision==False or time<=t:
        return [x01[0]+v1[0]*time,x01[1]+v1[1]*time, x02[0]+v2[0]*time,x02[1]+v2[1]*time]
    else:
        return [x1+v_1[0]*(time-t),y1+v_1[1]*(time-t),x2+v_2[0]*(time-t),y2+v_2[1]*(time-t)]
#==============================================================================
import pygame
from pygame.locals import *
import sys
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Collision")
clock=pygame.time.Clock()
FPS=60

t_now=0
while True:
    x_now=x(t_now)
    x1_now=x_now[0]
    y1_now=x_now[1]
    x2_now=x_now[2]
    y2_now=x_now[3]
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(x1_now,y1_now),r1)
    pygame.draw.circle(screen,(0,255,0),(x2_now,y2_now),r2)
    pygame.display.update()
    clock.tick(FPS)
    t_now+=1/FPS
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
