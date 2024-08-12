import pygame
import random
from typing import List, Tuple
from player import Player
from boardCreation import getFloor, drawFloor

def isCollidingWithRec(rect: dict, mousPos: Tuple[int, int]) -> bool:
    if ((rect.left <= mousePos[0] & mousePos[0] <= rect.right) &
        (rect.top <= mousePos[1] & mousePos[1] <= rect.bottom)):
        return True
    else:
        return False



pygame.init()

screenWidth = 1280
screenHeight = 720
screenSize = (screenWidth, screenHeight)

boardSize = 700
numCells = 10
cellSize = boardSize // numCells
cellWidth = cellSize
cellHeight = cellSize

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
running = True

startingX = (screenWidth - boardSize) // 2
startingY = (screenHeight - boardSize) // 2
startingPos = (startingX, startingY)
floor = getFloor(startingPos, (cellSize, cellSize), numCells)

player = Player("yellow", cellWidth - 10, cellHeight - 10, (cellSize, cellSize), floor, screen)
playerStartX = ((screenWidth - boardSize) // 2) + 5
playerStartY = ((screenHeight - boardSize) // 2) + 5
player.rect.topleft = (playerStartX, playerStartY)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if isCollidingWithRec(player.rect, mousePos):
                if not player.selected:
                    player.selected = True
            elif player.selected == True:
                attackInitialized = False
                for attack_key, attack_info in player.attacks.items():
                    if isCollidingWithRec(attack_info['rectangle'], mousePos):
                        player.initiateAttack(attack_key)
                        attackInitialized = True
                if not attackInitialized:
                    player.moove(mousePos)
                player.selected = False

    drawFloor(screen, floor)
    player.draw()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

