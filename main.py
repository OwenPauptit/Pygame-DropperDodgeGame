#Dropper Dodge Game

import pygame,random,sys

screenHeight = 480
screenWidth = 640
screen = pygame.display.set_mode((screenWidth,screenHeight))

class gameObject:
    def __init__(self,image,speed):
        self.image = image
        self.speed = speed
        if self.image == car:
            self.pos = image.get_rect().move(screenWidth-340,screenHeight-125)
        elif self.image == enemy:
            k = random.randint(0,screenWidth-30)
            self.pos = image.get_rect().move(k,0)
            self.active = True
    def move_right(self):
        global screenWidth
        self.pos = self.pos.move(self.speed,0)
        if self.pos.right > (screenWidth-5):
            self.pos = self.pos.move((-1*self.speed),0)
    def move_left(self):
        global screenWidth
        self.pos = self.pos.move((-1*self.speed),0)
        if self.pos.left < 5:
            self.pos = self.pos.move(self.speed,0)
    def fall(self):
        global screenHeight, difficulty, max_dif,dif_inc,enemies_dodged
        self.pos = self.pos.move(0,self.speed)
        if self.pos.bottom > (screenHeight-101):
            self.active = False
            enemies_dodged = enemies_dodged + 1
            if difficulty < max_dif-dif_inc*5:
                if difficulty > max_dif*0.75:
                    difficulty = round(difficulty+dif_inc/4,0)
                if difficulty > max_dif/2:
                    difficulty = round(difficulty + dif_inc/2,0)
                else:
                    difficulty = difficulty + dif_inc
                print ("Difficulty:",difficulty)
            elif difficulty < max_dif-dif_inc:
                if random.randint(0,1)and random.randint(0,1) and random.randint(0,1)and random.randint(0,1) and random.randint(0,1):
                    difficulty = difficulty + 1                    
                

def write_score(enemies_dodged):
    font = pygame.font.Font("8-BIT WONDER.ttf",18)
    label = font.render(("Enemies Dodged ( "+str(enemies_dodged)+" )"),1,(255,255,255))
    rect = pygame.Rect((0,380),(640,480))
    pygame.draw.rect(screen,(55,223,27),rect)
    screen.blit(label,(20,440))

def hscore(score):
    highscore = open("Highscore.txt","r").readline()
    if score > int(highscore):
        highscore = open("Highscore.txt","w")
        highscore.write(str(score))
        highscore.close()
        highscore = open("Highscore.txt","r").readline()
    font = pygame.font.Font("8-BIT WONDER.ttf",27)
    label = font.render(("Highscore ( "+highscore+" )"),1,(255,255,255))
    screen.blit(label,(140,310))  
        
    
           
playerSpeed = 3
enemySpeed = 1

gameover = pygame.image.load("gameover.png")
enemy = pygame.image.load("enemy.png")
car = pygame.image.load("BigCar.png")
background = pygame.image.load("Background-640x480px.png").convert()
player = gameObject(car,playerSpeed)
screen.blit(background,(0,0))
screen.blit(player.image,player.pos)
pygame.display.update()
direction = ""

enemies = []
difficulty = 0
max_dif = 100
dif_inc = 2
enemies_dodged = 0
pygame.init()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == ord("a"):
                direction = "left"
            if event.key == ord("d"):
                direction = "right"
        elif event.type == pygame.KEYUP:
            direction = ""
    screen.blit(background,player.pos,player.pos)
    if direction == "right":
        player.move_right()
    elif direction == "left":
        player.move_left()

    for x in enemies:
        if x.active:
            if x.pos.bottom >= player.pos.top:
                if (x.pos.right > player.pos.left and x.pos.right < player.pos.right) or (x.pos.left > player.pos.left and x.pos.left < player.pos.right):
                    screen.blit(gameover,(0,0))
                    screen.blit(player.image,player.pos)
                    font = pygame.font.Font("8-BIT WONDER.ttf",99)
                    label = font.render(str(enemies_dodged),1,(255,255,255))
                    labelpos = label.get_rect()
                    labelpos.center = (320,240)
                    screen.blit(label,labelpos)
                    hscore(enemies_dodged)
                    pygame.display.update()
                    print (pygame.time.get_ticks()*enemies_dodged*1000)
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit()
                            elif event.type == pygame.KEYDOWN:
                                import DropperGameCode
    
    newEnemy = random.randint(0,max_dif-difficulty)
    if newEnemy == 1:
        o = gameObject(enemy,(enemySpeed))
        enemies.append(o)
        newEnemy = 0
    for x in enemies:
        screen.blit(background,x.pos,x.pos)
        if x.active == True:           
            x.fall()
            screen.blit(x.image,x.pos)
            
    screen.blit(player.image,player.pos)
    write_score(enemies_dodged)
    
    pygame.display.update()
    pygame.time.delay(10)

