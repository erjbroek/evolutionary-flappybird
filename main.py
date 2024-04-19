import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

def generate_pipe():
  config.pipes.append(components.Pipes(config.win_width))

font = pygame.font.Font(None, 36)
def render_text(surface, text, position):
    rendered_text = font.render(text, True, (0, 0, 0))
    surface.blit(rendered_text, position)

def main():
  pipes_spawn_delay = 10

  while True:
    quit_game()

    config.window.fill((100, 150, 255))
    config.ground.render(config.window)

    if pipes_spawn_delay <= 0:
      generate_pipe()
      pipes_spawn_delay = 200
    pipes_spawn_delay -= 1

    for pipe in config.pipes:
      pipe.render(config.window)
      pipe.update(population)
      if pipe.off_screen:
        config.pipes.remove(pipe)

    if not population.extinct():
      population.update_players()
      if population.current_score >= 20:
        config.pipes.clear()
        population.current_score = 0
        population.natural_selection()
    else:
      config.pipes.clear()
      population.current_score = 0
      population.natural_selection()
    
    generation_text = f"Generation: {population.generation}"
    alive = 0
    for p in population.players:
      if p.alive:
        alive += 1
    amount_players = f"alive: {alive}"
    record = f"record: {population.highest_score}"
    current = f"current score: {population.current_score}"
    render_text(config.window, generation_text, (20, config.win_height - 50))
    render_text(config.window, amount_players, (20, config.win_height - 80))
    render_text(config.window, record, (20, config.win_height - 110))
    render_text(config.window, current, (20, config.win_height - 140))

    clock.tick(60)
    pygame.display.flip()

main()
