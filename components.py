import pygame
import random


class Ground:
  ground_posY = 500

  def __init__(self, win_width):
    self.x, self.y = 0, Ground.ground_posY
    self.rect = pygame.Rect(self.x, self.y, win_width, 5)

  def render(self, window):
    pygame.draw.rect(window, (255, 255, 255), self.rect)

class Pipes:
  width = 15
  opening_height = 100
  color = (255, 255, 255)

  def __init__(self, win_width):
    self.x = win_width
    self.bottom_height = random.randint(10, 300)
    self.top_height = Ground.ground_posY - self.bottom_height - self.opening_height
    self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
    self.passsed = False
    self.off_screen = False

  def render(self, window):
    self.bottom_rect = pygame.Rect(self.x, Ground.ground_posY - self.bottom_height, self.width, self.bottom_height)
    pygame.draw.rect(window, self.color, self.bottom_rect)

    self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
    pygame.draw.rect(window, self.color, self.top_rect)

  def update(self):
    self.x -= 1
    if self.x + Pipes.width <= 50:
      self.passed = True
      self.color = (255, 0, 255)

    if self.x + self.width <= 0:
      self.off_screen = True

