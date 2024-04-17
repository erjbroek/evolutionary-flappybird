import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(10)

def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

def generate_pipe():
  config.pipes.append(components.Pipes(config.win_width))

def main():
  pipes_spawn_delay = 10

  while True:
    quit_game()

    config.window.fill((0, 0, 0))
    config.ground.render(config.window)

    if pipes_spawn_delay <= 0:
      generate_pipe()
      pipes_spawn_delay = 200
    pipes_spawn_delay -= 1

    for pipe in config.pipes:
      pipe.render(config.window)
      pipe.update()
      if pipe.off_screen:
        config.pipes.remove(pipe)

    if not population.extinct():
      population.update_players()
    else:
      pass
    
    clock.tick(60)
    pygame.display.flip()

main()
