import pygame, sys,os,random,csv # import pygame and sys
import numpy as np
import pathlib
from pathlib import *
clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygame modules
import time
import zmq


##Gamevariables
run=True

directory_time = Path.cwd() /'Data_Time'
user_input=input("What's your name?:")
filepath_time = directory_time / user_input

# directory_collision="/home/isurana/Desktop/Robotics/Quarter-4/AEM/My_version/v1/Data_Collision/"
# user_input=input("What's your name?:")
# filepath_collision = directory_collision + user_input


def load_map(path):
    f=open(path+'.txt',"r")
    data=f.read()
    f.close()
    data=data.split('\n')
    game_map=[]
    for row in data:
        game_map.append(list(row))
    return game_map

game_map=load_map('map')


## Check for collision

def collision_test(rect, tiles):
    hit_list = []

    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    
            print("collision list",hit_list)
    return hit_list





def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:

        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    # print("Hit List",hit_list)
    # np.save(pathlib.Path(filepath_collision),hit_list) # save
    return rect, collision_types

time_list=[]
def score_display(game_state):
    if game_state=='main_game':
        score_surface=game_font.render(f'Time: {int(score)}',True,(255,255,255))
        score_rect=score_surface.get_rect(center=(525,50))
        display.blit(score_surface,score_rect)
        # print("Score",score)
        time_list.append(score)
        # print(time_list)


pygame.init() # initiate pygame

pygame.display.set_caption('Pygame Window') # set the window name

WINDOW_SIZE = (1200,800) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

display = pygame.Surface((600, 400))


pygame.mixer.music.load('music/music.wav')
pygame.mixer.music.play(-1)

player_image = pygame.image.load('images/drone_16.png')


roof_image = pygame.image.load('images/roof.png')
TILE_SIZE = roof_image.get_width()




dirt_image = pygame.image.load('images/tile2-m.png')
platform_image_up=pygame.image.load('images/tile-u.png')
platform_image_down=pygame.image.load('images/tile-d.png')
platform_image=pygame.image.load('images/platform.png')
coin_image=pygame.image.load('images/coin1.png')





clock=pygame.time.Clock()
game_font=pygame.font.Font('04B_19.TTF',20)

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0
true_scroll=[0,0]
scroll=[0,0]
player_rect = pygame.Rect(50, 250, player_image.get_width(), player_image.get_height())

# print("player position", player_image.rect)

test_rect = pygame.Rect(100,100,100,50)
collision_sound_timer=0
score=0
high_score=0
game_active=True


# def game_end(rect,tile):
#     for layer in game_map:
    
#         for tile in layer:
#             if tile == '6':
#                 if rect.colliderect(tile):
#                     print("HItting stff")


while run: # game loop

        
    true_scroll[0]+=(player_rect.x-scroll[0]-352)/20
    true_scroll[1]+=(player_rect.y-scroll[1]-206)/20
    scroll=true_scroll.copy()
    scroll[0]=int(scroll[0])
    scroll[1]=int(scroll[1])    
    
    display.fill((25,25,25))
    

    
        
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(roof_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '3':
                display.blit(platform_image_up, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '4':
                display.blit(platform_image_down, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '5':
                display.blit(platform_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '6':
                display.blit(coin_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                
    
            x += 1
        y += 1
        
    np.save(pathlib.Path(filepath_time),time_list) # save
    
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0
    # if player_y_momentum > 3:
        # player_y_momentum = 3

    # game_end(player_rect,tile_rects)


    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    # print("Player rect",player_rect)

    ## Bouncing in the opposite direction

    if collisions['bottom']:
        player_y_momentum=-0.5
        
    elif collisions['top']:
        player_y_momentum=1
        
    # if collisions['bottom']:
    #     player_y_momentum = 0
    #     air_timer = 0
    # else:
    #     air_timer += 1
        
        
    # print(hit_list)
        
    if game_active:
        score+=0.024
        score_display('main_game')

        
    display.blit(player_image, (player_rect.x-scroll[0], player_rect.y-scroll[1]))

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if event.type == KEYDOWN:
            if event.key==K_w:   ## Press w to fade the music put
                pygame.mixer.music.fadeout(1000)
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                player_y_momentum =-1
            if event.key==K_DOWN:
                player_y_momentum=+1
            if event.key==K_ESCAPE:
                run=False
                
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key==K_UP:
                    player_y_momentum += 0.2
                    if player_y_momentum > 3:
                        player_y_momentum = 3
            if event.key==K_DOWN:
                    player_y_momentum += 0.2
                    if player_y_momentum > 3:
                        player_y_momentum = 3
            
          
            

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(80) # maintain 90 fps
