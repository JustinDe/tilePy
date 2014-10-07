import mapFile
import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((mapFile.mapSize_X*mapFile.tileSize_X,mapFile.mapSize_Y*mapFile.tileSize_Y))
pygame.display.set_caption("Map Parse")

x_cord = 0
y_cord = 0
m_count = 0

for node in range(0,len(mapFile.map)):
	for mat in range(0,len(mapFile.mats)):
		if mapFile.map[node] == mapFile.mats[mat][0]:
			#print mapFile.mats[mat][1]
			#print '('+str(x_cord)+', '+str(y_cord)+')'
			screen.blit(pygame.image.load(mapFile.mats[mat][1]),(x_cord,y_cord))
			x_cord += mapFile.tileSize_X
			m_count += 1
			if m_count >= mapFile.mapSize_X:
				y_cord += mapFile.tileSize_Y
				x_cord = 0
				m_count = 0

active = True
while active:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = False
	pygame.display.update()
pygame.quit()