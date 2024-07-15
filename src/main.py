# Example file showing a circle moving on screen
import pygame
import random
import threading


# pygame setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
disabled_game = False
list_cubes = []
position_ocuped = []
cube_stopped = True

def drawBoard():
    cube_position_y = 50
    cube_position_x = 60
    cube_size = 80
    group = 0

    for element in range(16):
        if(group == 4):
            cube_position_y = cube_position_y+cube_size
            cube_position_x = 60
            group = 0

        pygame.draw.rect(screen,[187, 173, 161, 255],(cube_position_x,cube_position_y,cube_size,cube_size))

        cube_position_x = cube_position_x+cube_size
        group = group + 1

class CubeWithNumber():
    def __init__(self, x, y, size, number):
        self.x = x
        self.y = y
        self.size = size
        self.number = number
        self.stoped = False

    def draw(self, screen):

        if self.number == 2:
            rect_color = (238, 227, 218, 255)
        elif self.number == 4:
            rect_color = (237, 222, 201, 255)
        elif self.number == 8:
            rect_color = (254, 203, 171, 255)
        elif self.number == 16:
            rect_color = (254, 166, 138, 255)
        elif self.number == 32:
            rect_color = (255, 132, 106, 255)
        elif self.number > 32:
            rect_color = (255, 97, 76, 255)

        pygame.draw.rect(screen, tuple(rect_color), (self.x, self.y, self.size, self.size))
        
        text_surface = font.render(str(self.number), True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))

        screen.blit(text_surface, text_rect)

    def get_number(self):
        return self.number
    
def create_cube():
    global disabled_game
    x = 60
    y = 50
    size = 80
    number = 2
    while True:
        random_numberX = random.randint(0,3)
        random_numberY = random.randint(0,3)

        match random_numberX:
            case 0:
                x = 60
            case 1:
                x = 140
            case 2:
                x = 220
            case 3:
                x = 300

        match random_numberY:
            case 0:
                y = 50
            case 1:
                y = 130
            case 2:
                y = 210
            case 3:
                y = 290

        if not [x,y] in position_ocuped:
            position_ocuped.append([x,y])
            break

    square = CubeWithNumber(x, y, size, number)
    list_cubes.append(square)
    disabled_game = False
def draw_cubes(screen):
    global position_ocuped
    position_ocuped = [[cube.x,cube.y] for cube in list_cubes]
    for square in list_cubes:
        square.draw(screen)


def move_up():
    number = 0
    for cube in list_cubes:
        cube.stopped = False

    while not all(cube.stopped for cube in list_cubes):
        cube.y = cube.y-1

        for position in position_ocuped:
            if cube.x == position[0] and cube.y < position[1] + 80:
                cube.y = position[1] + 80
                cube.stopped = True
                number = number + 1

        if cube.y < 50:
            cube.y = 50
            cube.stopped = True
            number = number + 1
        


        if len(list_cubes) == number:
            break

    
    threading.Timer(0.5, create_cube).start()

def keydown(move):
    global disabled_game

    if (not disabled_game): 
        disabled_game = True 
        match move:
            case "up":
                move_up()
            case "down":
                move_down = True
            case "left":
                move_left = True
            case "right":
                move_right = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    pygame.draw.rect(screen, (119,111,103,255), (50, 40, 340, 340))

    drawBoard()
    draw_cubes(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        keydown("up")
    if keys[pygame.K_s]:
        keydown("down")
    if keys[pygame.K_a]:
        keydown("left")
    if keys[pygame.K_d]:
        keydown("right")
    
    if len(list_cubes) == 0:
        create_cube()

    if len(position_ocuped) == 16:
        running = False

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
