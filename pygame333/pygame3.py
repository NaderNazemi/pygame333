# This is condensed version of pygame2.py - game is a barebone version and works.
import pygame, time, random
pygame.init()
display_width, display_height = 800, 600
black, white, block_color = (0,0,0), (255,255,255), (53,115,255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (50,50))
car_width = 50

def car(x, y): # create car 
    gameDisplay.blit(carImg, (x, y))

def message_display(text): # when car crashes
    font = pygame.font.Font('freesansbold.ttf', 80)
    gameDisplay.blit(font.render(text, True, (0,0,0)), (display_width/7, display_height/2))
    pygame.display.update()
    time.sleep(2)
    game_loop()

def things(thing_x, thing_y, thing_w, thing_h, color): # create blocks 
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

def things_dodged(counter): # dodge counter 
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(counter), True, black)
    gameDisplay.blit(text, (0,0))

def game_loop():  
    x_change = 0
    x = (display_width*0.45)
    y = (display_height*0.9)
    thing_x_start = random.randrange(0, display_width)
    thing_y_start = -600
    thing_width, thing_height = 50, 50
    thing_speed = 4
    dodged = 0
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get(): # event handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -10
                if event.key == pygame.K_RIGHT:
                    x_change += +10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
        
        x += x_change # game logic handling
        gameDisplay.fill(white) 
        car(x, y) # function - draw car
        things(thing_x_start, thing_y_start, thing_width, thing_height, block_color) # function - draw blocks 
        thing_y_start = thing_y_start + thing_speed
        things_dodged(dodged) # function to increment 'dodged' display
        
        if (x > display_width - car_width) or (x < 0): # when car hits the screen edges (left, right)
            message_display('You Crashed')
        if (thing_y_start > display_height): # when a block passes the screen
            thing_y_start = 0 - thing_height
            thing_x_start = random.randrange(0, display_width-thing_width)
            dodged += 1 
            if dodged % 2 == 0:
                thing_speed += 1   
        if (thing_y_start + thing_height > y) and (thing_x_start < x + car_width) and (thing_x_start + thing_width > x): # when car hits block 
            message_display('You Crashed')
                
        pygame.display.update()
        clock.tick(120)
game_loop()    
#%%

