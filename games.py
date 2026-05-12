import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_option("Space Shooter")

# Background
Background = pygame.image.load("maroon.jpg")
Background = pygame.transform.scale(Background, (WIDTH, HEIGHT))

# Player
Player = pygame.image.load("sapu_ijuk.png")
Player = pygame.transform.scale(Player, (80, 80))

# Enemy
Enemy = pygame.image.load("jjaemu.png")
Enemy = pygame.transform.scale(Enemy, (80, 80))