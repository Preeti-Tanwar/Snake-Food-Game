import pygame
import random
import os
pygame.mixer.init()

x=pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snake_size = 10
fps = 30
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_list,snk_size):
    # print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size, snake_size])
#creating welcome screen
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((157,224,230))
        text_screen("Welcome To Snakes Game", black, 170, 170)
        text_screen("Press Space Bar To Play", black, 200, 250)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("snake walking.mp3")
                    pygame.mixer.music.play(-1)
                    game_loop()
        pygame.display.update()
        clock.tick(fps)

#creating game window
clock=pygame.time.Clock()
gameWindow=pygame.display.set_mode((900,500))
#background image
bgimg=pygame.image.load("snake background image.jpg")
bgimg=pygame.transform.scale(bgimg,(900,500)).convert_alpha()
pygame.display.set_caption("This is snake Game")
pygame.display.update()
font = pygame.font.SysFont('georgia', 50)

#game loop
def game_loop():
    # game specific vatiables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20, 880)
    food_y = random.randint(20, 480)
    init_velocity = 5
    snk_list = []
    snk_length = 1
    #check if highscore file exist
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            # gameover background
            gameover_img = pygame.image.load("game over image.jpg")
            gameover_img = pygame.transform.scale(gameover_img, (900, 500)).convert_alpha()

            gameWindow.blit(gameover_img,(0,0))
            text_screen("Press Enter To Cont..",red,240,350)
            text_screen("Your Score:"+str(score), red,300,400)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load("snake walking.mp3")
                        pygame.mixer.music.play(-1)
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key==pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key==pygame.K_q:
                        score=score+10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x = random.randint(20, 880)
                food_y = random.randint(20, 480)
                snk_length+=1
                if score>int(highscore):
                    highscore=score
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: " +str(score)+ "  Highscore: "+str(highscore),red,5,5)
            # pygame.draw.rect(gameWindow,black,[snake_x , snake_y , snake_size , snake_size])

            pygame.draw.rect(gameWindow,red,[food_x,food_y , snake_size , snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
                pygame.mixer.music.load("explode sound.mp3")
                pygame.mixer.music.play()
                # print("game over")
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("explode sound.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()