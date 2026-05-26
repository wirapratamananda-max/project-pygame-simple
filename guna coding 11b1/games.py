import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Background
Background = pygame.image.load("maroon.jpg")
Background = pygame.transform.scale(Background, (WIDTH, HEIGHT))

# Player
Player = pygame.image.load("sapu_ijuk.png")
Player = pygame.transform.scale(Player, (80, 80))
player_X = WIDTH // 2
player_Y = HEIGHT - 100
Player_speed = 10

# Enemy
Enemy = pygame.image.load("jjaemu.png")
Enemy = pygame.transform.scale(Enemy, (80, 80))
Enemy_speed = 10 
Enemy_Y = 0
Enemy_X = random.randint(0, WIDTH - 80)

# Bullet
Bullet = pygame.image.load("sapu_ijuk.png")
Bullet = pygame.transform.scale(Bullet, (10, 50))
Bullet_speed = 100
Bullets = []

score = 0
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tembak
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_X = player_X + 35
                bullet_Y = player_Y
                Bullets.append([bullet_X, bullet_Y])

        # Gerak Player
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT] and player_X > 0:
            player_X -= 5
        if Keys[pygame.K_RIGHT] and player_X < WIDTH - 80:
            player_X += 5
        if Keys[pygame.K_UP] and player_Y > 0:
            player_Y -= 5
        if Keys[pygame.K_DOWN] and player_Y < HEIGHT - 80:
            player_Y += 5

        Enemy_Y += Enemy_speed
        if Enemy_X > WIDTH:  
            Enemy_X = 0
            Enemy_Y = random.randint(0, HEIGHT- 80)

        # Peluru
        for bullet in Bullets:
            bullet[1] -= Bullet_speed

        Bullets = [bullet for bullet in Bullets if bullet[1] > 0]

        enemy_rect = pygame.Rect(Enemy_X, Enemy_Y, 60, 60)
        for bullet in Bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], 10, 50)
            if enemy_rect.colliderect(bullet_rect):
                score += 1
                Enemy_X = random.randint(0, WIDTH - 80)
                Enemy_Y = 0
                Bullets.remove(bullet)

        # Collision player vs musuh
        player_rect = pygame.Rect(player_X, player_Y, 60, 60)
        if player_rect.colliderect(enemy_rect):
            print('Game Over!')
            pygame.quit()
            sys.exit0()

        #Render
        screen.blit(Background, (0,0))
        screen.blit(Player, (player_X, player_Y))
        screen.blit(Enemy, (Enemy_X, Enemy_Y))

        for bullet in Bullets:
            screen.blit(Bullet, ((bullet[0]), bullet[1]))

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(50)