import pygame


def builder(screen, mf, gridlines):
    if mf.mapSize_X*mf.mapSize_Y == len(''.join(mf.mapLine.split())):
        x_cord = 0
        y_cord = 0
        for i, mapLine in enumerate(mf.mapLine):
            for mat in mf.mats:
                if mf.mapLine[i] == mat[0]:
                    screen.blit(pygame.image.load(mat[1]), (x_cord, y_cord))
                    x_cord += mf.tileSize_X
                    if x_cord > ((mf.mapSize_X-1)*mf.tileSize_X):
                        y_cord += mf.tileSize_Y
                        x_cord = 0
                    break
    else:
        font = pygame.font.Font(None, 30)
        maperrorlbl = font.render("ACSII render error - Check mapFile.py", 1, (255, 255, 255))
        screen.blit(maperrorlbl, (10, mf. screen_Y/2))

    if gridlines:
        gl_x = 0
        gl_y = 0
        #vertical gridlines
        for lineV in range(0, (mf.mapSize_X-1)):
            pygame.draw.rect(screen, (0, 0, 0), ((mf.tileSize_X+gl_x)-1, 0, 2, mf.mapSize_Y*mf.tileSize_Y))
            gl_x += mf.tileSize_X
        #horizontal gridlines
        for lineH in range(0, (mf.mapSize_Y-1)):
            pygame.draw.rect(screen, (0, 0, 0), (0, (mf.tileSize_Y+gl_y)-1, mf.mapSize_X*mf.tileSize_Y, 2))
            gl_y += mf.tileSize_Y
