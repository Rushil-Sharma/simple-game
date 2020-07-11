import pygame 
import sys
import random

pygame.init()

height = 600
width  = 800

my_sprite_colour = (0,200,255)
my_sprite_size = (50)
bgcolour = (0,0,0)
my_sprite_position = [400,height-2*my_sprite_size]

enemy_size = 50
enemy_position = [random.randint(0,width-enemy_size), 0]
enemy_colour = (255,0,0 )
enemy_speed = 15
enemy_list = [enemy_position]

screen = pygame.display.set_mode((width,height))

game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace",35)

score = 0

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay > 0.9:
        x_pos = random.randint(0,width-enemy_size)
        y_pos = random.randint(0,1)
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, enemy_colour, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))

def update_enemy_position(enemy_list,score):
    for idx,enemy_position in enumerate(enemy_list):
        if enemy_position[1] >= 0 and enemy_position[1] < height:
            enemy_position[1] +=  enemy_speed 
            screen.fill(bgcolour)  

        else:
            score += 1
            enemy_list.pop(idx)
    return score

def collision_check(enemy_list,my_sprite_position):
    for enemy_position in enemy_list:
        if detect_collision(enemy_position,my_sprite_position):
            return True
    return False


def detect_collision(my_sprite_position,enemy_position):
    m_s_x = my_sprite_position[0]
    m_s_y = my_sprite_position[1]

    e_x = enemy_position[0]
    e_y = enemy_position[1]


    if (e_x >= m_s_x and e_x <= (m_s_x + my_sprite_size)) or (m_s_x >= e_x and m_s_x <= (e_x + my_sprite_size)):
        if (e_y >= m_s_y and e_y <= (m_s_y + my_sprite_size)) or (m_s_y >= e_y and m_s_y <= (e_y + my_sprite_size)):
            return  True

    return False 

while not game_over:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        

        if event.type == pygame.KEYDOWN:
    
            x = my_sprite_position[0]
            y = my_sprite_position[1]
            
            if event.key == pygame.K_LEFT:
                x -= my_sprite_size
            elif event.key == pygame.K_RIGHT:
                x += my_sprite_size

            screen.fill(bgcolour)
            my_sprite_position = (x,y)

    drop_enemies(enemy_list)
    score = update_enemy_position(enemy_list,score)

    text = "Score:" + str(score)
    lable = myFont.render(text,1,(255,255,0))
    screen.blit(lable,(width-200,height-40))

    if collision_check(enemy_list,my_sprite_position):
        game_over = True
    draw_enemies(enemy_list)
    pygame.draw.rect(screen, my_sprite_colour, (my_sprite_position[0], my_sprite_position[1], my_sprite_size, my_sprite_size))

    clock.tick(30)

    if score == 500:
        game_over = True
        print("you beat the game !*!*!*!*!*!")  
    else:
        print()  

    pygame.display.update()  

if score >= 100:
    print("you reached till",score,"and that is more than 100 good !" )
elif score >= 200:
    print("you reached till",score,"and that is more than 200 nice !!" )
elif score >= 300:
    print("you reached till",score,"and that is more than 300 awesome !!!" )
elif score >= 400:
    print("you reached till",score,"and that is more than 400 terrific !!" )     
elif score >= 50:
    print("you reached the",score," level and that is more than 50 awesome !" )
else:
    print ("your score is ",score)


