import pygame
def builder(screen,mf):
	print "map_X: "+str(mf.mapSize_X)
	print "map_Y: "+str(mf.mapSize_Y)
	print "mapLine_cnt: "+str(len(''.join(mf.mapLine.split())))
	if(mf.mapSize_X*mf.mapSize_Y == len(''.join(mf.mapLine.split()))):

		x_cord = 0
		y_cord = 0

		for node in range(0,len(mf.mapLine)):
			for mat in mf.mats:
				if mf.mapLine[node] == mat[0]:
					screen.blit(pygame.image.load(mat[1]),(x_cord,y_cord))
					x_cord += mf.tileSize_X
					if x_cord > ((mf.mapSize_X-1)*mf.tileSize_X):
						y_cord += mf.tileSize_Y
						x_cord = 0
					break
	else:
		font=pygame.font.Font(None,30)
		mapErrorLbl=font.render("ACSII render error - Check mapFile.py", 1,(255,255,255))
		screen.blit(mapErrorLbl, (10, mf.screen_Y/2))