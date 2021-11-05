from pygame.locals import *
import pygame

from PixelMap import PixelMap
from MapBuffer import MapBuffer
from Player import Player

pygame.init()
pygame.font.init()

HEIGHT = 600
WIDTH = 600
FPS = 120

default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 45)
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural map generation")
FramePerSec = pygame.time.Clock()

world = PixelMap(3000, 300)
player = Player(50, 0., 0.)
view = MapBuffer(world, player.x, player.y)

displaysurface.fill((255,255,255))
displaysurface.blit(view.get_surface(player.x, player.y), (0, 0))

mask = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
mask.fill((0,0,0, 255))
pygame.draw.circle(mask, (255,255,255, 0), (WIDTH//2, HEIGHT//2), min(HEIGHT,WIDTH)//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_z:
                player.set_speed('up')

            if event.key == pygame.K_s:
                player.set_speed('down')

            if event.key == pygame.K_q:
                player.set_speed('left')

            if event.key == pygame.K_d:
                player.set_speed('right')
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_z:
                player.reset_speed('up')

            if event.key == pygame.K_s:
                player.reset_speed('down')

            if event.key == pygame.K_q:
                player.reset_speed('left')

            if event.key == pygame.K_d:
                player.reset_speed('right')

    dT = FramePerSec.tick(FPS)
    player.update_position(dT/1000)
    label = font_renderer.render(str(round(FramePerSec.get_fps())), True, (255,255,255))

    displaysurface.blit(view.get_surface(player.x, player.y), (0, 0))
    displaysurface.blit(mask, (0,0))
    displaysurface.blit(label, label.get_rect())
    
    pygame.display.update()