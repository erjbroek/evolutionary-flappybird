import pygame
import random
import config


class Ground:
  ground_posY = 500

  def __init__(self, win_width):
    self.x, self.y = 0, Ground.ground_posY
    self.rect = pygame.Rect(self.x, self.y, win_width, config.win_height - self.y)
    self.grass = pygame.Rect(self.x, self.y, win_width, 30)

  def render(self, window):
    pygame.draw.rect(window, (255, 255, 255), self.rect)
    pygame.draw.rect(window, (50, 200, 100), self.grass)


class Pipes:
  width = 55
  opening_height = 100
  color = (50, 150, 50)

  def __init__(self, win_width):
    self.x = 500
    self.bottom_height = random.randint(10, 300)
    self.top_height = Ground.ground_posY - self.bottom_height - self.opening_height
    self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
    self.passed = False
    self.off_screen = False

  def render(self, window):
    # also renders ceiling:
    ceiling = pygame.Rect(0, 0, 550, 10)
    pygame.draw.rect(window, (255, 255, 255), ceiling)

    self.bottom_rect = pygame.Rect(self.x, Ground.ground_posY - self.bottom_height, self.width, self.bottom_height)
    pygame.draw.rect(window, self.color, self.bottom_rect)

    self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
    pygame.draw.rect(window, self.color, self.top_rect)

  def update(self, population):
    self.x -= 2
    if self.x + Pipes.width <= 50 and not self.passed:
      self.passed = True
      self.color = (50, 200, 50)
      population.passed = True

    if self.x <= -self.width:
      self.off_screen = True

