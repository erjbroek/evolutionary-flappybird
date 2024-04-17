import pygame
import random
import config

class Player:
  def __init__(self):
    self.x, self.y = 50, 200
    self.rect = pygame.Rect(self.x, self.y, 20, 20)
    self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
    self.velocity = 0
    self.jump = False
    self.alive = True

    self.decision = None


  def render(self, window):
    pygame.draw.rect(window, self.color, self.rect)

  def ground_collision(self, ground):
    return pygame.Rect.colliderect(self.rect, ground)
  
  def ceiling_collision(self):
    return bool(self.y <= 30)
  
  def pipe_collision(self):
    for pipe in config.pipes:
      return pygame.Rect.colliderect(self.rect, pipe.top_rect) or pygame.Rect.colliderect(self.rect, pipe.bottom_rect)
    
  def update(self, ground):
    if not (self.ground_collision(ground) or self.pipe_collision()):
      self.velocity += 0.5
      self.rect.y += self.velocity
      if self.velocity > 7:
        self.velocity = 7
    else:
      self.alive = False
      self.jump = False
      self.velocity = 0
  
  def bird_jump(self):
    if not self.jump and not self.ceiling_collision():
      self.jump = True
      self.velocity = -7
    if self.velocity >= 3:
      self.jump = False

  def think(self):
    self.decision = random.uniform(0, 1)
    if self.decision > 0.73:
      self.bird_jump()