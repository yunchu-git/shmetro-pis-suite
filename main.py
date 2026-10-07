import pygame
import LCD
pygame.init()
pygame.display.set_mode((800,600))
pygame.display.set_caption("上海地铁模拟器")
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
pygame.quit()