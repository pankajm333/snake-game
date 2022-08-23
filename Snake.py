# import pygame
# x= pygame.init()
#
# #creating window
# gameWindow = pygame.display.set_mode((1200,500))
# pygame.display.set_caption("My firts Game - Blank")
#
# #game specific variables
# exit_game =False
# game_over = False
#
# # Creating a game loop
# while not exit_game:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             exit_game = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 print("You have pressed right arrow key")
# pygame.quit()
# quit()

import  pygame
import random

pygame.init()

#Colours
white =(255,255,255)
red =(255,0,0)
black =(0,0,0)

#creating window
screen_width =700
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width,screen_height))


# Game Tittle
pygame.display.set_caption("Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list ,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color , [x,y, snake_size, snake_size])



#Game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if hiscore == '':
            hiscore = 0

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 30
    while not  exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue",red,100,200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.k_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                       velocity_x = - 10
                       velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 10
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x =0

            snake_x = snake_x + velocity_x
            snake_y =  snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score


            gameWindow.fill(white)
            text_screen("Score:" + str(score ) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                 game_over =True
                 print("Game Over")
          # pygame.draw.rect(gameWindow, black,[snake_x,snake_y, snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()