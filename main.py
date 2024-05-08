import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(25)

def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

def generate_pipe():
  config.pipes.append(components.Pipes(config.win_width))

font = pygame.font.Font(None, 25)
def render_text(surface, text, position):
    rendered_text = font.render(text, True, (0, 0, 0))
    surface.blit(rendered_text, position)

def main():
  pipes_spawn_delay = 0

  while True:
    quit_game()

    config.window.fill((100, 150, 255))
    config.ground.render(config.window)

    if pipes_spawn_delay <= 0:
      generate_pipe()
      pipes_spawn_delay = 200
    pipes_spawn_delay -= 1

    for pipe in config.pipes:
      pipe.update(population)
      pipe.render(config.window)
      if pipe.off_screen:
        config.pipes.remove(pipe)

    if config.pipes:
      if not population.extinct():
        # if population.current_score >= 30:
        #   config.pipes.clear()
        #   population.current_score = 0
        #   population.natural_selection()

        population.update_players()
        average_weight1 = 0
        average_weight2 = 0
        average_weight3 = 0
        average_vision1 = 0
        average_vision2 = 0
        average_vision3 = 0
        average_decision = 0
        amount_alive = len([player for player in population.players if player.alive])
        for player in population.players:
          if player.alive:
            average_weight1 += player.brain.connections[0].weight / amount_alive
            average_weight2 += player.brain.connections[1].weight / amount_alive
            average_weight3 += player.brain.connections[2].weight / amount_alive
            average_vision1 += player.vision[0] / amount_alive
            average_vision2 += player.vision[1] / amount_alive
            average_vision3 += player.vision[2] / amount_alive
            average_decision += player.decision / amount_alive

        vision1 = f"{round(average_vision1, 1)}"
        vision2 = f"{round(average_vision2, 1)}"
        vision3 = f"{round(average_vision3, 1)}"
        if average_decision > 0.73:
          decision = "jump"
        else:
          decision = "no jump"

        pygame.draw.circle(config.window, (255, 255, 255), (370, 100), 20)
        pygame.draw.circle(config.window, (255, 255, 255), (370, 170), 20)
        pygame.draw.circle(config.window, (255, 255, 255), (370, 240), 20)
        pygame.draw.circle(config.window, (255, 255, 255), (500, 170), 20)
        pygame.draw.line(config.window, (min(255 * abs(average_weight1), 255), 0, 0), (370, 100), (500, 170), round(10 * average_weight1))
        pygame.draw.line(config.window, (min(255 * abs(average_weight2), 255), 0, 0), (370, 170), (500, 170), round(10 * average_weight2))
        pygame.draw.line(config.window, (min(255 * abs(average_weight3), 255), 0, 0), (370, 240), (500, 170), round(10 * average_weight3))
        render_text(config.window, vision1, (360, 100))
        render_text(config.window, vision2, (360, 170))
        render_text(config.window, vision3, (360, 240))
        render_text(config.window, decision, (490, 170))
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
    amount_species = f"species: {len(population.species)}"
    render_text(config.window, generation_text, (20, config.win_height - 50))
    render_text(config.window, amount_players, (20, config.win_height - 80))
    render_text(config.window, record, (20, config.win_height - 110))
    render_text(config.window, current, (20, config.win_height - 140))
    render_text(config.window, amount_species, (250, config.win_height - 140))

    clock.tick(300)
    pygame.display.flip()

main()
