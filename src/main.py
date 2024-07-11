# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
game_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
disabled_game = False

def transform_board(array,type):
    match type:
        case 'vertical':
            game_board = []

def gerarCube():
   while True:
        numero_aleatorio = random.randint(0, 15)
        if game_board[numero_aleatorio] == 0:
            game_board[numero_aleatorio] = 2
            break
    

def move(move):
    global disabled_game
    

    if (not disabled_game): 
        disabled_game = True 
        match move:
            case "up":
                gerarCube()                
                


def drawBoard():
    cube_position_y = 50
    cube_position_x = 60
    cube_size = 80
    group = 0

    for element in game_board:
        if(group == 4):
            cube_position_y = cube_position_y+10+cube_size+10
            cube_position_x = 60
            group = 0
        if element == 0:
            cube_color = [187, 173, 161, 255]
        if element == 2:
            cube_color = [238,227,218,255]
        if element == 4:
            cube_color = [237,222,201,255]
        if element == 8:
            cube_color = [254,203,171,255]
        if element == 16:
            cube_color = [254,166,138,255]
        if element == 32:
            cube_color = [255,132,106,255]
        if element > 32:
            cube_color = [255,97,76,255]

        pygame.draw.rect(screen,tuple(cube_color),(cube_position_x,cube_position_y,cube_size,cube_size))

        if(element>0):
            text_surface = font.render(str(element), True, (120,99,77,255))
            text_rect = text_surface.get_rect(center=(cube_position_x + cube_size // 2, cube_position_y + cube_size // 2))
            screen.blit(text_surface, text_rect)
        cube_position_x = cube_position_x+10+cube_size+10
        group = group + 1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    pygame.draw.rect(screen, (119,111,103,255), (50, 40, 410, 410))

    drawBoard()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move("up")
    if keys[pygame.K_s]:
        move("down")
    if keys[pygame.K_a]:
        move("left")
    if keys[pygame.K_d]:
        move("right")
    

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
