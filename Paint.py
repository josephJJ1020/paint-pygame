import sys

import pygame
pygame.init()

pygame.font.init()
font = pygame.font.SysFont("rockwell", 20)

screensize = width, height = 500, 500
screen = pygame.display.set_mode(screensize)

red = (255,0,0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0,0,255)
indigo = (75, 0, 130)
white = (255,255,255)
black = (0,0,0)

canvasSize = cw, ch = 500, 400
squaresize = (50,50)

screen.fill([50,50,50])
background = pygame.Rect((0,0), canvasSize)
pygame.draw.rect(screen, white, background)

canvas = pygame.Rect((0,0), (cw, ch -10))
pygame.draw.rect(screen, white, canvas)


circlesize = 5

def drawBackground(rect):
    pygame.draw.rect(screen, white, rect)

currentcolor = black
pressed = False

while 1:
    menu = pygame.draw.rect(screen, (50, 50, 50), (0, 400, width, height - ch))

    redsquare = pygame.Rect((squaresize[0], ch + 20), squaresize)
    pygame.draw.rect(screen, red, redsquare)

    orangesquare = pygame.Rect((squaresize[0] * 2, ch + 20), squaresize)
    pygame.draw.rect(screen, orange, orangesquare)

    yellowsquare = pygame.Rect((squaresize[0] * 3, ch + 20), squaresize)
    pygame.draw.rect(screen, yellow, yellowsquare)

    greensquare = pygame.Rect((squaresize[0] * 4, ch + 20), squaresize)
    pygame.draw.rect(screen, green, greensquare)

    bluesquare = pygame.Rect((squaresize[0] * 5, ch + 20), squaresize)
    pygame.draw.rect(screen, blue, bluesquare)

    indigosquare = pygame.Rect((squaresize[0] * 6, ch + 20), squaresize)
    pygame.draw.rect(screen, indigo, indigosquare)

    blacksquare = pygame.Rect((squaresize[0] * 7, ch + 20), squaresize)
    pygame.draw.rect(screen, black, blacksquare)

    whitesquare = pygame.Rect((squaresize[0] * 8, ch + 20), squaresize)
    pygame.draw.rect(screen, white, whitesquare)

    up = pygame.Rect((15, ch + 20), (25, 25))
    pygame.draw.rect(screen, white, up)

    down = pygame.Rect((15, ch + 50), (25, 25))
    pygame.draw.rect(screen, white, down)

    size = font.render(str(circlesize), True, white)
    sizerect = size.get_rect()
    sizerect.x = 0
    sizerect.y = ch
    sizetext = screen.blit(size, sizerect)

    pos = pygame.mouse.get_pos()  # get cursor coordinates

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # reset canvas
                drawBackground(background)
                circlesize = 5
                currentcolor = black

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True

        if event.type == pygame.MOUSEBUTTONDOWN and up.collidepoint(pos):
            circlesize += 1

        if event.type == pygame.MOUSEBUTTONDOWN and down.collidepoint(pos):
            circlesize -= 1

        if event.type == pygame.MOUSEBUTTONDOWN and redsquare.collidepoint(pos):
            currentcolor = red

        if event.type == pygame.MOUSEBUTTONDOWN and orangesquare.collidepoint(pos):
            currentcolor = orange

        if event.type == pygame.MOUSEBUTTONDOWN and yellowsquare.collidepoint(pos):
            currentcolor = yellow

        if event.type == pygame.MOUSEBUTTONDOWN and greensquare.collidepoint(pos):
            currentcolor = green

        if event.type == pygame.MOUSEBUTTONDOWN and bluesquare.collidepoint(pos):
            currentcolor = blue

        if event.type == pygame.MOUSEBUTTONDOWN and indigosquare.collidepoint(pos):
            currentcolor = indigo

        if event.type == pygame.MOUSEBUTTONDOWN and blacksquare.collidepoint(pos):
            currentcolor = black
            
        if event.type == pygame.MOUSEBUTTONDOWN and whitesquare.collidepoint(pos):
            currentcolor = white


        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False

        if event.type == pygame.MOUSEMOTION and pressed and canvas.collidepoint(pos):
            pygame.draw.circle(screen, currentcolor, pos, circlesize)


    pygame.display.update()