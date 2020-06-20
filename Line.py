import pygame
import random
import pyautogui as gui
import pyscreenshot
pygame.init()

width=1920
height=1080

game_display=pygame.display.set_mode((400,400))

clock = pygame.time.Clock()


def screenshot():
    screenshot=pyscreenshot.grab()
    screenshot.save('Test Screenshot for Line Program')
    





def draw_line():
    

    x=random.randint(0,255)
    y=random.randint(0,255)
    z=random.randint(0,255)

    width_start=random.randint(1,width)
    height_start=random.randint(1,height)

    width_end=random.randint(1,400)
    height_end=random.randint(1,400)
    
    random_length=random.randint(1,10)
    color=(x,y,z)
    pygame.draw.line(game_display, color, (width_start,height_start), (width_end,height_end), random_length )

black=(0,0,0)
i=0
game_display.fill(black)
    
while True:
 
    if i%10==0:
        draw_line()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
		  
    pygame.display.update()
    clock.tick(500)
    i+=1






