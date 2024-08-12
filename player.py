import pygame
from typing import Tuple, List

class Player(pygame.sprite.Sprite):
    def __init__(self, color: str, width: int, height: int, cellSize: Tuple[int, int], floor: List[dict], surface: dict):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.floor = floor
        self.selected = False
        self.cellSize = cellSize
        self.movementRange = 2
        self.surface = surface
        self.attacks = self.getAttacks()
        self.attackSelected = False
        self.lifePoints = 10
        self.wasOnBadCell = False

    def  moove(self, wantedPosition: Tuple[int, int]):
        allowedCells = self.getPlayerAllowedCells()
        for cell in allowedCells:
            if (((cell['rectangle'].left <= wantedPosition[0]) & (wantedPosition[0] <= cell['rectangle'].right)) &
                ((cell['rectangle'].top <= wantedPosition[1]) & (wantedPosition[1] <= cell['rectangle'].bottom))):
                self.rect.center = cell['rectangle'].center
                self.wasOnBadCell = False
        self.selected = False
    
    def getPlayerAllowedCells(self) -> List[dict]:
        allowedCells = []
        allowedMovementSize = (self.cellSize[0] * self.movementRange, self.cellSize[1] * self.movementRange)
        
        playerLeftLimit = self.rect.left - allowedMovementSize[0] - (self.rect.width // 2)
        playerRightLimit = self.rect.right + allowedMovementSize[0] + (self.rect.width // 2)
        playerTopLimit = self.rect.top - allowedMovementSize[1] - (self.rect.height // 2)
        playerBottomLimit = self.rect.bottom + allowedMovementSize[1] + (self.rect.height // 2)
        
        for cell in self.floor:
            cellRect = cell['rectangle']
            if (playerLeftLimit <= cellRect.center[0] <= playerRightLimit and
                playerTopLimit <= cellRect.center[1] <= playerBottomLimit):
                allowedCells.append(cell)    
        return allowedCells

    def getAttacks(self) -> List[dict]:
        attacks = {}
        surfaceSize = list(self.surface.get_size())
        surfaceSize[0] = (surfaceSize[0] // 5) * 4
        surfaceSize[1] = surfaceSize[1] // 5
        for i in range(3):
            attack = pygame.Rect(surfaceSize[0], surfaceSize[1], 100, 100)
            attacks[f'attack_{i}'] = {'rectangle': attack, 'color': 'white', 'active': False}
            surfaceSize[1] += 150

        return attacks

    def initiateAttack(self, attack_key) -> None:
        self.attacks[attack_key]['color'] = "red"

    def isOnBadCell(self) -> bool:
        returnValue = False
        if not self.wasOnBadCell:
            for cell in self.floor:
                if self.rect.colliderect(cell['rectangle']) and cell['color'] == 'red':
                    returnValue = True
                    self.wasOnBadCell = True
        return returnValue

    def update(self) -> None:
        pass

    def draw(self):
        self.surface.blit(self.image, self.rect)
        if self.selected:
            allowedCells = self.getPlayerAllowedCells()
            for cell in allowedCells:
                pygame.draw.rect(self.surface, 'yellow', cell['rectangle'], 1)
                
        for attack_key, attack_info in self.attacks.items():
            color = attack_info['color']
            rectangle = attack_info['rectangle']
            image = pygame.Surface((rectangle.width, rectangle.height))
            image.fill(color)
            self.surface.blit(image, rectangle)
