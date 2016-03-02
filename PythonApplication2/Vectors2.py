import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
PURPLE=(255,0,255)
CYAN=(0,255,255)

PI = math.pi

SCREEN_X=400
SCREEN_Y=500
FOCUS=200

colourlist=(RED,GREEN,BLUE,WHITE,YELLOW,PURPLE,CYAN)

screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
pygame.display.set_caption("Python App")

def polydraw(faces,colour,size):
    def convert(face):
        pointlist=[]
        for vertex in face:
            x=((FOCUS*vertex[0])/(FOCUS+vertex[2]))+(SCREEN_X/2)
            y=(SCREEN_Y/2)-((FOCUS*vertex[1])/(FOCUS+vertex[2]))
            pointlist.append((x,y))
        return pointlist

    facedepths=[]
    for i, face in enumerate(faces):
        zsum=0
        for j, vertex in enumerate(face):
            zsum=zsum+vertex[2]
        facedepths.append((i,zsum/(j+1)))
    facedepths=sorted(facedepths, key=lambda x: x[1], reverse=True)

    for depth in facedepths:
        pointlist=convert(faces[depth[0]])
       
        lightcolour=[0,0,0]
        for i in range(3):
            brightness=colour[i]-(colour[i]*((depth[1]+size)/(2*size)))
            
            
            lightcolour[i]=brightness
        pygame.draw.polygon(screen,lightcolour,pointlist,0)

def polyspin(faces,rotation):
    for face in faces:
        for vertex in face:
            x=vertex[0]
            y=vertex[1]
            z=vertex[2]
            xSin=rotation[0][0]
            xCos=rotation[0][1]
            ySin=rotation[1][0]
            yCos=rotation[1][1]
            zSin=rotation[2][0]
            zCos=rotation[2][1]
            
           
            z1=(z*xCos)-(y*xSin)
            y1=(y*xCos)+(z*xSin)
            z=z1
            y=y1

            x1=(x*yCos)-(z*ySin)            
            z1=(z*yCos)+(x*ySin)
            x=x1
            z=z1

            y1=(y*zCos)-(x*zSin)
            x1=(x*zCos)+(y*zSin)
            y=y1
            x=x1
      
            vertex[0]=x    
            vertex[1]=y
            vertex[2]=z
    return faces      

class cube(object):
    def __init__(self,size):
        self.size=size
        self.colour=WHITE
        self.verticies=[[-size,size,size],
                        [size,size,size],
                        [size,size,-size],
                        [-size,size,-size],
                        [-size,-size,size],
                        [size,-size,size],
                        [size,-size,-size],
                        [-size,-size,-size]]

        self.faces=[[self.verticies[0],self.verticies[1],self.verticies[2],self.verticies[3]],
                   [self.verticies[0],self.verticies[3],self.verticies[7],self.verticies[4]],
                   [self.verticies[0],self.verticies[1],self.verticies[5],self.verticies[4]],
                   [self.verticies[6],self.verticies[5],self.verticies[1],self.verticies[2]],
                   [self.verticies[6],self.verticies[7],self.verticies[3],self.verticies[2]],
                   [self.verticies[6],self.verticies[7],self.verticies[4],self.verticies[5]]]

        self.rotation=[(math.sin(0.0),math.cos(0.0)),(math.sin(0.0),math.cos(0.0)),(math.sin(0.0),math.cos(0.0))]

    def setRotation(self,x,y,z):
        self.rotation=[(math.sin(x),math.cos(x)),(math.sin(y),math.cos(y)),(math.sin(z),math.cos(z))]

    def draw(self):
        polydraw(self.faces,self.colour,self.size)

    def rotate(self):
        self.faces=polyspin(self.faces,self.rotation)

    def setColour(self,colour):
        self.colour=colour

mycube=cube(50.0)
mycube.setRotation(0.005,0.007,0.009)
mycube.setColour(BLUE)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill(BLACK)
    mycube.draw()
    mycube.rotate()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

 

 

 