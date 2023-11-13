import pygame
import sys
from Game import TheGame

pygame.init()

Screen = pygame.display.set_mode((512, 512))

CurrentGame = TheGame(Screen,6,50,1)

CurrentGame.StartGame()

pygame.quit()
sys.exit()