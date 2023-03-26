import pygame
import os

pygame.font.init()


WIDTH,HEIGHT=2000,1050
WIND = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first game")

WHITE = (255,255,255)
BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 70)
WINNER_FONT = pygame.font.SysFont('comicsans', 200)

FPS = 60
VEL = 9
BULLET_VELOCITY = 30
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2
space =pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")), (WIDTH, HEIGHT)) 

SPACESHIP_WIDTH,SPACESHIP_HEIGHT=160,90
yellow_spaceshipImg = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
yellow_spaceship = pygame.transform.scale(yellow_spaceshipImg, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
yellow_spaceship =  pygame.transform.rotate(yellow_spaceship,90)
red_spaceshipImg = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
red_Spaceship = pygame.transform.scale(red_spaceshipImg, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
red_Spaceship = pygame.transform.rotate(red_Spaceship,270)



def draw_window(yellow,red, yellow_bullets,red_bullets,yellow_health,red_health,winner_text):
    WIND.blit(space,(0,0))
    red_health_text = HEALTH_FONT.render(str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render(str(yellow_health), True, WHITE)
    winner_text_text = WINNER_FONT.render(winner_text, True, WHITE)
    WIND.blit (red_health_text,(WIDTH - red_health_text.get_width() -50,  30))
    WIND.blit(yellow_health_text, (50, 30))
    
    WIND.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIND.blit(red_Spaceship,(red.x,red.y))
    pygame.draw.rect(WIND,(0,0,0),BORDER) # black border
    
    for bullet in yellow_bullets:
          pygame.draw.rect(WIND,(255,255,0),bullet) # yellow bullet
    for bullet in red_bullets:
          pygame.draw.rect(WIND,(255,0,0),bullet) # red bullet    
     
    pygame.display.update()

def move_yellow(yellow,keys_pressed):
     if keys_pressed[pygame.K_a]: #left
            yellow.x= yellow.x - VEL
     if keys_pressed[pygame.K_d]: #right
            yellow.x+=VEL
     if keys_pressed[pygame.K_w]: #up
            yellow.y =yellow.y - VEL
     if keys_pressed[pygame.K_s]: #down
            yellow.y+=VEL

def print_winner(winner_text):
   winner_text_text = WINNER_FONT.render(winner_text, True, WHITE)
   WIND.blit(winner_text_text,(WIDTH//2 - winner_text_text.get_width()/2 , HEIGHT//2 - winner_text_text.get_height()/2))
   pygame.display.update()
   pygame.time.delay(5000)

def move_red(red,keys_pressed):
    if keys_pressed[pygame.K_UP]: #up
         red.y = red.y - VEL
    if keys_pressed[pygame.K_DOWN]: #down
         red.y+=VEL
    if keys_pressed[pygame.K_LEFT]: #left
         red.x = red.x - VEL
    if keys_pressed[pygame.K_RIGHT]: #right
         red.x+=VEL

def handle_bullets (yellow_bullets,red_bullets,yellow_spaceship,red_Spaceship):
        
        for bullet in yellow_bullets:

                bullet.x+=BULLET_VELOCITY
                if bullet.x<0 or bullet.x>WIDTH:
                        yellow_bullets.remove(bullet)
                if red_Spaceship.colliderect(bullet):
                        pygame.event.post(pygame.event.Event(RED_HIT))
                        yellow_bullets.remove(bullet)
        for bullet in red_bullets:
                bullet.x -=BULLET_VELOCITY
                if bullet.x<0 or bullet.x>WIDTH:
                    red_bullets.remove(bullet)
                if yellow_spaceship.colliderect(bullet):
                       pygame.event.post(pygame.event.Event(YELLOW_HIT))
                       red_bullets.remove(bullet)
                   



def handle_offscreen(yellow,red):
    if yellow.x < 0:
            yellow.x = 0
    if yellow.x > WIDTH-SPACESHIP_WIDTH:
            yellow.x = WIDTH-SPACESHIP_WIDTH
    if red.x < 0:
            red.x = 0
    if red.x > WIDTH-SPACESHIP_WIDTH+50:
            red.x = WIDTH-SPACESHIP_WIDTH+50
    if yellow.y < 0:
             yellow.y = 0
    if yellow.y > HEIGHT-SPACESHIP_HEIGHT -40:
            yellow.y = HEIGHT-SPACESHIP_HEIGHT -40
    if red.y < 0:
            red.y = 0
    if red.y > HEIGHT-SPACESHIP_HEIGHT -40:
            red.y = HEIGHT-SPACESHIP_HEIGHT -40
    if yellow.x > WIDTH/2-70:
          yellow.x = WIDTH/2-70
    if red.x < WIDTH/2+5:
          red.x = WIDTH/2+5


def main():
    yellow = pygame.Rect(400,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(1600,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets =[]
    yellow_bullets =[]
    red_health =10
    yellow_health =10
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN :
                  if event.key == pygame.K_q  and len(yellow_bullets) < MAX_BULLETS :
                        yellow_bullet = pygame.Rect(yellow.x+yellow.width,yellow.y + yellow.height//2 -2 ,30,15)
                        yellow_bullets.append(yellow_bullet)
                        
                  if event.key == pygame.K_BACKSLASH and len(red_bullets) < MAX_BULLETS :
                        red_bullet= pygame.Rect(red.x ,red.y + red.height//2 -2,30,15)
                        red_bullets.append(red_bullet)
            if event.type == YELLOW_HIT:
                 yellow_health-=1      # red hit yellow
            if event.type == RED_HIT:
                red_health-=1       # yellow hit red
        winner_text=""
        if red_health<=0:
             winner_text = "YELLOW WINS!"
        if yellow_health<=0:
              winner_text = "RED WINS!" 
        if winner_text!= "":    
                print_winner(winner_text)
                red_bullets =[]
                yellow_bullets =[]
                break
         
      

       
        keys_pressed = pygame.key.get_pressed()
        move_yellow(yellow,keys_pressed)
        move_red(red,keys_pressed)
        handle_offscreen(yellow,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(yellow,red,yellow_bullets,red_bullets ,yellow_health,red_health,winner_text)
    main()  

if __name__ == '__main__':
    main()