import brain
import pygame
import random
import config


class Player:
  def __init__(self, color = None, posY = None):
    # Bird
    self.x, self.y = 50, 300
    self.rect = pygame.Rect(self.x, self.y, 20, 20)
    self.color = color if color else (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    self.vel = 0
    self.jump = False
    self.alive = True
    self.lifespan = 0
    self.passed = False
    self.species_index = None

     # AI
    self.decision = 0
    self.vision = [0.5, 1, 0.5]
    self.fitness = 0
    self.inputs = 3
    self.brain = brain.Brain(self.inputs)
    self.brain.generate_net()


  def render(self, window):
    pygame.draw.rect(window, self.color, self.rect)
    if self.species_index is not None and self.alive:
      font = pygame.font.Font(None, 24)
      text = font.render(str(self.species_index), True, (255, 255, 255))
      window.blit(text, (self.x, self.rect.y - 30))

  def set_y(self, y):
    self.y = y
    self.rect.y = y

  def ground_collision(self, ground):
    return pygame.Rect.colliderect(self.rect, ground)
  
  def sky_collision(self):
    return bool(self.rect.y < 10)
  
  def pipe_collision(self):
    for pipe in config.pipes:
      return pygame.Rect.colliderect(self.rect, pipe.top_rect) or pygame.Rect.colliderect(self.rect, pipe.bottom_rect)
    
  def update(self, ground):
    if not (self.ground_collision(ground) or self.pipe_collision() or self.sky_collision()):
      self.vel += 0.25
      self.rect.y += self.vel
      if self.vel > 8:
        self.vel = 8

      self.lifespan += 1
    else:
      self.alive = False
      self.jump = False
      self.vel = 0
      self.rect.x -= 2
  
  def bird_jump(self):
    if not self.jump and not self.sky_collision():
      self.jump = True
      self.vel = -5.5
    if self.vel >= 1:
      self.jump = False

  @staticmethod
  def closest_pipe():
    for p in config.pipes:
      if not p.passed:
        return p

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
                      (self.rect.center[0], config.pipes[0].bottom_rect.top))

  def think(self):
    self.decision = self.brain.feed_forward(self.vision)
    if self.decision > 0.73:
      self.bird_jump()

  def calculate_fitness(self):
    self.fitness = self.lifespan

  def clone(self):
    clone = Player()
    clone.fitness = self.fitness
    clone.brain = self.brain.clone()
    clone.brain.generate_net()
    return clone
