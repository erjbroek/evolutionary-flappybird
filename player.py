import brain
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
    self.vision = [0.5, 1, 0.5]
    self.inputs = 3
    self.brain = brain.Brain(self.inputs)
    self.brain.generate_net()


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

  @staticmethod
  def closest_pipe():
    for pipe in config.pipes:
      if not pipe.passed:
        return pipe

  def look(self):
    if config.pipes:

      #line to top pipe
      self.vision[0] = max(0, self.rect.center[1] - self.closest_pipe().top_rect.bottom) / 500
      pygame.draw.line(config.window, self.color, self.rect.center, 
                      (self.rect.center[0], config.pipes[0].top_rect.bottom))
      
      # Line to mid pipe
      self.vision[1] = max(0, self.closest_pipe().x - self.rect.center[0]) / 500
      pygame.draw.line(config.window, self.color, self.rect.center, 
                      (config.pipes[0].x, self.rect.center[1]))
      
      #line to bottom pipe
      self.vision[2] = max(0, self.closest_pipe().bottom_rect.top - self.rect.center[1]) / 500
      pygame.draw.line(config.window, self.color, self.rect.center, 
                      (self.rect.center[0], config.pipes[0].top_rect.bottom))

  def think(self):
    self.decision = self.brain.feed_forward(self.vision)
    if self.decision > 0.73:
      self.bird_jump()