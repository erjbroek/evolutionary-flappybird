import pygame


class Ground:
  ground_posY = 500

  def __init__(self, win_width):
    self.x, self.y = 0, Ground.ground_posY
    self.rect = pygame.Rect(self.x, self.y, win_width, 5)

  def render(self, window):
    pygame.draw.rect(window, (255, 255, 255), self.rect)
