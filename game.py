import pygame
import tilePy
import mapFile as mf

pygame.init()
pygame.display.set_caption("Map Parse")
screen = pygame.display.set_mode((mf.screen_X,mf.screen_Y))

#builder(drawing surface, map file, gridline (t/f))
tilePy.builder(screen,mf,True)

active = True
while active:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = False
	pygame.display.update()
pygame.quit()
