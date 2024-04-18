import operator
import random
class Species:
  def __init__(self, player):
    self.players = []
    self.avg_fitness = 0
    self.threshold = 1.2
    self.players.append(player)
    self.benchmark_fitness = player.fitness
    self.benchmark_brain = player.brain.clone()
    self.champion = player.clone()
    self.staleness = 0
    self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)

  def similarity(self, brain):
    # compares brain of a bird with benchmark brain of species
    similarity = self.weight_difference(self.benchmark_brain, brain)
    return self.threshold > similarity
  

  @staticmethod
  def weight_difference(brain1, brain2):
    #sums up absolute differences between connection weights of both brains
    # if they are similar, they are put in the same species
    total_weight_difference = 0
    for i in range(0, len(brain1.connections)):
      for j in range(0, len(brain2.connections)):
        if i == j:
          total_weight_difference += abs(brain1.connections[i].weight - brain2.connections[j].weight)
    return total_weight_difference
  
  def add_to_species(self, player):
    self.players.append(player)

  def sort_players_by_fitness(self):
    # sorts the player by fitness, and makes the player with the highest fitness the champion
    self.players.sort(key=operator.attrgetter('fitness'), reverse=True)
    if self.players[0].fitness > self.benchmark_fitness:
      self.staleness = 0
      self.benchmark_fitness = self.players[0].fitness
      self.champion = self.players[0].clone()
    else:
      self.staleness += 1

  def calculate_average_fitness(self):
    total_fitness = 0
    for player in self.players:
      total_fitness += player.fitness
      #checks if there are players
    if self.players:
      self.avg_fitness = int(total_fitness / len(self.players))
    else:
      self.avg_fitness = 0

  def offspring(self):
    # player with index 0 is already cloned, since it's the champion
    baby = self.players[random.randint(1, len(self.players)) - 1].clone()

    #mutation
    baby.brain.mutate()
    return baby
