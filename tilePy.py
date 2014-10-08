import pygame
def builder(screen,mf,gridLines):
	#print "map_X: "+str(mf.mapSize_X)
	#print "map_Y: "+str(mf.mapSize_Y)
	#print "mapLine_cnt: "+str(len(''.join(mf.mapLine.split())))

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

	if gridLines == True:
		#pygame.draw.rect(screen,(255,255,255),(50,0,4,400))
		gl_X = 0
		gl_Y = 0
		#vertical grid lines
		for lineV in range(0,(mf.mapSize_X-1)):
			pygame.draw.rect(screen,(0,0,0),((50+gl_X)-1,0,2,mf.mapSize_Y*mf.tileSize_Y))
			gl_X += 50

		for lineH in range(0,(mf.mapSize_Y-1)):
			pygame.draw.rect(screen,(0,0,0),(0,(50+gl_Y)-1,mf.mapSize_X*mf.tileSize_Y,2))
			gl_Y += 50
