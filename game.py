import pygame,random,time

from player import Player
from obstacles import moving_obstacle
from obstacles import fixed_obstacle
pygame.init()

Black = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
Red = ( 255, 0, 0)
Green = ( 0, 255, 0)
blue = (0,0,255)
lime = ((180,255,100))

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

#screen
display_width = 1000
display_height = 800

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('River Crossing')



all_sprites_list = pygame.sprite.Group()
#player
x = "monkey.png"
player1 = Player(70,60,50,x)
player1.rect.x = (display_width * 0.45)
player1.rect.y = (display_height * 0.9)

x = "frog2.jpg"
player2 = Player(60,50,50,x)
player2.rect.x = (display_width * 0.45)
player2.rect.y = (display_height * 0)

all_sprites_list.add(player1)
all_sprites_list.add(player2)


#start end
font = pygame.font.SysFont("comicsansms", 50)
start = font.render("START", True, (0, 0, 0))
end = font.render("END", True, (0, 0, 0))



score1 =  0
score2 = 0
font = pygame.font.SysFont("comicsansms", 50)
Score1 = font.render('player1 : ' + str(score1), True, (0, 0, 0))
Score2 = font.render('player2 : ' + str(score2), True, (0, 0, 0))

#players turn
font = pygame.font.SysFont("comicsansms", 30)
turn1 = font.render("player1's turn", True, (0, 0, 0))
turn2 = font.render("player2's turn", True, (0, 0, 0))


#fixed_objects

all_fixed_obs = pygame.sprite.Group()

for j in range (1,5):
    for i in range(0,5):
        fobs = fixed_obstacle(Black, 50, 50)
        fobs.rect.x = 80 + (i * 200)  
        fobs.rect.y = 0 + (j * 150)
        all_fixed_obs.add(fobs)
        all_sprites_list.add(fobs)

#moving_objects

all_coming_obs = pygame.sprite.Group()

for j in range (0,6):
    for i in range (random.randint(1,3),random.randint(6,8)):
        mobs = moving_obstacle(random.choice(colorList), 80, 60,20)
        mobs.rect.x = 0 +  i * 250
        mobs.rect.y = 60 + j * 150

        all_sprites_list.add(mobs)
        all_coming_obs.add(mobs)


#crashed message

def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.flip()

    time.sleep(2)  

    gameloop()      

def crash():
    message_display('You Crashed')

    gameloop()

speed = 1
f = 1
player  = player1
score1 = 0
score2 = 0
#game
def gameloop():

    global f
    global player
    global score1
    global score2

    if f == 1:
        f = 0
        player = player1
    else:
        if player == player1:
            player = player2
        else:
            player = player1        
    
    clock = pygame.time.Clock()

    player1.rect.x = (display_width * 0.45)
    player1.rect.y = (display_height * 0.92)

    player2.rect.x = (display_width * 0.45)
    player2.rect.y = (display_height * 0)

    xf = 0
    xm = 0
    f = 0

    q = False

    while not q:
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q = True
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)

        if keys[pygame.K_UP]:
            player.moveUp(5)
            xm = xm + 5
            xf = xf + 5
            #print(xm)
            #print(player2.rect.y)
        if keys[pygame.K_DOWN]:
            player.moveDown(5)
            xm = xm - 5
            xf = xf - 5
            #print(xm)
            #print(player.rect.y)
        
        
        if xm >=50 and xf >=200:
            xf = 0       
            score1 = score1 + 5   
            print(score1)      
           

        if xm >= 150:                    
            score1 = score1 + 10
            xm = 0
            print(score1)
           

        if xm <= -150:
            score2 = score2 + 10
            xm = 0
        
        if xm <= -50 and xf <=-200:
            xf = 0       
            score2 = score2 + 5  
        

        screen.fill(WHITE)

        
        x = 0
        for i in range(1,7):
            pygame.draw.rect(screen,lime,[0,0+x,1000,50])
            x += 150

        if player == player1:
            screen.blit(turn1,(850 ,10 ))
        else:
            screen.blit(turn2,(850 ,10 ))

        for obs in all_coming_obs:
            obs.move(speed)
            if obs.rect.x > display_width:
                obs.repaint(random.choice(colorList))
                obs.rect.x = 0

        collision_list = pygame.sprite.spritecollide(player,all_coming_obs,False)
        for obs in collision_list:
            print("crash")
            if player == player1:
                message_display('player1 crashed')

            else:
                message_display('player2 crashed')

        fixed_collision_list = pygame.sprite.spritecollide(player,all_fixed_obs,False)
        for obs in fixed_collision_list:
            print("fixed crash")
            if player == player1:
                message_display('player1 crashed')

            else:
                message_display('player2 crashed')
                

        all_sprites_list.draw(screen)

        Score1 = font.render('player1 : ' + str(score1), True, (0, 0, 0))
        Score2 = font.render('player2 : ' + str(score2), True, (0, 0, 0))
        screen.blit(Score1,( 800,780 ))
        screen.blit(Score2,(800,750))

        

        if player == player1:
            if player1.rect.y <= 1:
                message_display('you win')
            screen.blit(start,(0 , 800-start.get_height() ))
            screen.blit(end,(0, 50-end.get_height() ))
        elif player == player2:
            if player2.rect.y >= 760:
                message_display('player2 win')
            screen.blit(end,(0 , display_height-40))
            screen.blit(start,(0 ,0 ))

        if player == player1:
            screen.blit(start,(0 , 800-start.get_height() ))
            screen.blit(end,(0, 50-end.get_height() ))
        elif player == player2:
            screen.blit(end,(0 , display_height-40))
            screen.blit(start,(0 ,0 ))
   
        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()
