import pygame
import math
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
FOCUS=200

SCREEN_X=700
SCREEN_Y=500

def cube(size):
    global vX,vY,vZ,numpoints
    numpoints=8
    vX=[0-size,size,size  ,0-size,0-size,size  ,size  ,0-size]
    vY=[size  ,size,size  ,size  ,0-size,0-size,0-size,0-size]
    vZ=[size  ,size,0-size,0-size,size  ,size  ,0-size,0-size]
    
def drawcube(thickness):
    global sX, sY, vZ

 
    faceZ = [[0,(vZ[0]+vZ[2]/2)], [1,((vZ[0]+vZ[5])/2)],[2,((vZ[0]+vZ[7])/2)],[3,((vZ[6]+vZ[3])/2)],[4,((vZ[6]+vZ[1])/2)],[5,((vZ[6]+vZ[4])/2)]]

    faceZ=sorted(faceZ, key=lambda x: x[1],reverse=True)

    def drawcubeface(face):
        global sX, sY
        if face==0:
            pygame.draw.polygon(screen, RED,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[2],sY[2]),(sX[3],sY[3])],0)    
            pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[2],sY[2]),(sX[3],sY[3])],thickness)
        if face==1:
            pygame.draw.polygon(screen, WHITE,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[5],sY[5]),(sX[4],sY[4])],0)
            pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[5],sY[5]),(sX[4],sY[4])],thickness)
        if face==2:
            pygame.draw.polygon(screen, GREEN,[(sX[0],sY[0]),(sX[3],sY[3]),(sX[7],sY[7]),(sX[4],sY[4])],0)
            pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[3],sY[3]),(sX[7],sY[7]),(sX[4],sY[4])],thickness)
        if face==3:
            pygame.draw.polygon(screen, WHITE,[(sX[3],sY[3]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[7],sY[7])],0) 
            pygame.draw.polygon(screen, BLACK,[(sX[3],sY[3]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[7],sY[7])],thickness) 
        if face==4:
            pygame.draw.polygon(screen, BLUE,[(sX[1],sY[1]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[5],sY[5])],0)
            pygame.draw.polygon(screen, BLACK,[(sX[1],sY[1]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[5],sY[5])],thickness)
        if face==5:
            pygame.draw.polygon(screen, WHITE,[(sX[4],sY[4]),(sX[5],sY[5]),(sX[6],sY[6]),(sX[7],sY[7])],0)
            pygame.draw.polygon(screen, BLACK,[(sX[4],sY[4]),(sX[5],sY[5]),(sX[6],sY[6]),(sX[7],sY[7])],thickness)

    
    for i in range(6):
        drawcubeface(faceZ[i][0])    

    #pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[2],sY[2]),(sX[3],sY[3])],thickness)
    #pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[3],sY[3]),(sX[7],sY[7]),(sX[4],sY[4])],thickness)
    #pygame.draw.polygon(screen, BLACK,[(sX[4],sY[4]),(sX[5],sY[5]),(sX[6],sY[6]),(sX[7],sY[7])],thickness)
    #pygame.draw.polygon(screen, BLACK,[(sX[0],sY[0]),(sX[1],sY[1]),(sX[5],sY[5]),(sX[4],sY[4])],thickness)
    #pygame.draw.polygon(screen, BLACK,[(sX[1],sY[1]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[5],sY[5])],thickness)
    #pygame.draw.polygon(screen, BLACK,[(sX[3],sY[3]),(sX[2],sY[2]),(sX[6],sY[6]),(sX[7],sY[7])],thickness)    








def convert():
    global vX,vY,vZ,sX,sY,numpoints,FOCUS,SCREEN_X,SCREEN_Y
    sX=[0]*numpoints
    sY=[0]*numpoints
    for i in range(numpoints):
        sX[i]=((FOCUS*vX[i])/(FOCUS+vZ[i]))+(SCREEN_X/2)
        sY[i]=SCREEN_Y-(((FOCUS*vY[i])/(FOCUS+vZ[i]))+(SCREEN_Y/2))

def spinX(amt):
    global vX,vY,vZ,numpoints
    for i in range(numpoints):
        r=math.sqrt((math.pow(vY[i],2)+math.pow(vZ[i],2)))
        if vY[i]>0:
            ang=math.asin(vZ[i]/r)
        else:
            ang=math.pi-(math.asin(vZ[i]/r))
        ang=ang+amt
        vZ[i]=r*(math.sin(ang))
        vY[i]=r*(math.cos(ang))


def spinZ(amt):
    global vX,vY,vZ,numpoints
    for i in range(numpoints):
        r=math.sqrt((math.pow(vX[i],2)+math.pow(vY[i],2)))
        if vX[i]>0:
            ang=math.asin(vY[i]/r)
        else:
            ang=math.pi-(math.asin(vY[i]/r))
        ang=ang+amt
        vY[i]=r*(math.sin(ang))
        vX[i]=r*(math.cos(ang))
            

def spinY(amt):
    global vX,vY,vZ,numpoints
    for i in range(numpoints):
        r=math.sqrt((math.pow(vX[i],2)+math.pow(vZ[i],2)))
        if vX[i]>0:
            ang=math.asin(vZ[i]/r)
        else:
            ang=math.pi-(math.asin(vZ[i]/r))
        ang=ang+amt
        vZ[i]=r*(math.sin(ang))
        vX[i]=r*(math.cos(ang))


cube(35)
 

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("3D Vector")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # Draw on the screen a green line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    spinX(0.05)
    spinY(0.05)
    spinZ(0.05)
    convert()
    drawcube(2)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(50)
 
# Close the window and quit.
pygame.quit()