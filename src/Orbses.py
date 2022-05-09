#########################################
#    __  ____  ____  ____  ____  ____   #
#   /  \(  _ \(  _ \/ ___)(  __)/ ___)  #
#  (  O ))   / ) _ (\___ \ ) _) \___ \  #
#   \__/(__\_)(____/(____/(____)(____/  #
#                                       #
# Cameron Ross  |   Started: 2022/05/06 #
#                                       #
#                                       #
#########################################
# Update Notes
# V0.0 (05/06) 
# -Made a window open
# -Changed window title to "Orbses"
# -Changed window icon
# -Started Orb class
#
# V0.1 (05/08)
# -Window is now resizable
# -Added grey background
# -Added methods to orb class
# -Updated game loop
# -Clicking and dragging now creates an orb object which moves based on the distance of the drag
# -Made code prettier?

#### SETUP ####

from tkinter.tix import MAX
import pygame,sys,random
pygame.init()



## CONSTANTS ##

WIDTH, HEIGHT = 852, 480

WORLD = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
ICON = pygame.image.load("assets/orbses1.png")



## SCREEN SETUP ## 

pygame.display.set_caption("Orbses")
pygame.display.set_icon(ICON)

WORLD.fill((127,127,127))
pygame.display.flip()
clock = pygame.time.Clock()



#### CLASSES ####

class Orb:

    ## ATTRIBUTES ##

    pos = pygame.Vector2()
    vel = pygame.Vector2()
    color = (0, 0, 0)
    rad = 0
    field = 0


    ## CLASS METHODS ##

    # CONSTRUCTORS #

    def __init__(self):
        self.hor = 0
        self.ver = 0
        self.rad = 0
        self.color = (0, 0, 0)
        self.field = 0
        self.velX = 0
        self.velY = 0

        self.pos = pygame.Vector2()
        self.pos.xy = self.hor, self.ver
        self.pos[:] = self.hor, self.ver

        self.vel = pygame.Vector2()
        self.vel.xy = self.velX, self.velY
        self.vel[:] = self.velX, self.velY

    def __init__(self, h, v, r, f, c, vx, vy):
        self.hor = h
        self.ver = v
        self.rad = r
        self.color = c
        self.field = f
        self.velX = vx
        self.velY = vy

        self.pos = pygame.Vector2()
        self.pos.xy = self.hor, self.ver
        self.pos[:] = self.hor, self.ver

        self.vel = pygame.Vector2()
        self.vel.xy = self.velX, self.velY
        self.vel[:] = self.velX, self.velY

    # DRAWING #

    def drawSelf(self):
        pygame.draw.circle(WORLD, self.color, self.pos, self.rad)
        pygame.draw.circle(WORLD, (255,255,255), self.pos, self.field, width=1)

    # SETTERS #

    def updatePos(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def updateVelX(self, x):
        self.vel.x = x

    def flipVelX(self):
        self.vel.x *= -1

    def updateVelY(self, y):
        self.vel.y = y

    def flipVelY(self):
        self.vel.y *= -1



#### MAIN LOOP ####
   
def main():

    ## VARIABLES ##

    mouse_start = None

    ## MAIN LOOP ##

    while True:

        for event in pygame.event.get():

            # EXIT GAME #

            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()

            # PRESS MOUSE #
            if event.type == pygame.MOUSEBUTTONDOWN:

                if mouse_start is None:

                    mouse_start = pygame.mouse.get_pos()
                    pygame.mouse.get_rel()

                test = Orb(mouse_start[0], mouse_start[1], 7, 63, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 0, 0)
            #print(mouse_start) #DEBUG

            if event.type == pygame.MOUSEBUTTONUP and mouse_start is not None:

                drag = pygame.mouse.get_rel()
                vx = (drag[0]/10)*-1
                vy = (drag[1]/10)*-1
                test.updateVelX(vx)
                test.updateVelY(vy)
                mouse_start = None

        # REFRESH SCREEN #

        WORLD.fill((165,165,165))

        try:                    #   This is basically just
            test                #   making sure that the test 
        except NameError:       #   object exists before doing 
            test_exists = False #   anything with it.
        else:                   #
            test_exists = True  #

        if test_exists:

            test.updatePos()
            test.drawSelf()

            if mouse_start is not None:

                pygame.draw.line(WORLD, (255, 255, 255), mouse_start, pygame.mouse.get_pos(), width=5)

            if ((test.pos.x + test.rad) >= WORLD.get_width()) or ((test.pos.x - test.rad) <= 0):    #   If the ball object touches or goes 
                test.flipVelX()                                                                     #   past an edge, its velocity is to  
            if ((test.pos.y + test.rad) >= WORLD.get_height()) or ((test.pos.y - test.rad) <= 0):   #   reverse in that direction.
                test.flipVelY()                                                                     #

        pygame.display.flip()

        # DEBUG #

        #print (test.pos)
        #print (test.rad)
        #print("tick " + str(pygame.time.get_ticks()))

        clock.tick(60)



#### MAIN GUARD ####

if __name__ == "__main__":
    main()