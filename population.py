import config
import player
import math
import species
import operator

class Population:
  def __init__(self, size):
    self.players = []
    self.generation = 1
    self.species = []
    self.size = size
    self.furthest = 0
    self.highest_score = 0
    self.current_score = 0
    self.passed = False
    for i in range(0, self.size):
      self.players.append(player.Player())

  def update_players(self):
    for player in self.players:
      if player.alive:
        player.look()
        player.think()
        player.render(config.window)
        player.update(config.ground)
    self.check_scores()

  def natural_selection(self):
    print('speciate')
    self.speciate()

    print("calculate fitness")
    self.calculate_fitness()

    print("kill extinct")
    self.kill_extinct_species()

    print('kill stale species')
    self.kill_stale_species()

    print ("sort by fitness")
    self.sort_species_by_fitness()

    print("children creation")
    self.next_gen()

  def check_scores(self):
    if self.passed:
      self.passed = False
      self.current_score += 1
      if self.current_score >= self.highest_score:
        self.highest_score = self.current_score

    for player in self.players:
      if player.lifespan > self.furthest:
        self.furthest = player.lifespan
    

  def speciate(self):
    for s in self.species:
      s.players = []

    for player in self.players:
      add_to_species = False
      for s in self.species:
        if s.similarity(player.brain):
          s.add_to_species(player)
          player.color = s.color
          add_to_species = True
          break
      if not add_to_species:
        new_species = species.Species(player)
        player.color = new_species.color
        self.species.append(new_species)

  def calculate_fitness(self):
    for player in self.players:
      player.calculate_fitness()
    for s in self.species:
      s.calculate_average_fitness()

  def kill_extinct_species(self):
    species_bin = []
    for s in self.species:
      if len(s.players) == 0:
        species_bin.append(s)
    for s in species_bin:
      self.species.remove(s)

  def kill_stale_species(self):
    player_bin = []
    species_bin = []
    for s in self.species:
      if s.staleness >= 8:
        if len(self.species) > len(species_bin) + 1:
          species_bin.append(s)
          for player in s.players:
            player_bin.append(player)
        else:
          s.staleness = 0
    for player in player_bin:
      self.players.remove(player)
    for s in species_bin:
      self.species.remove(s)
    
    

  def sort_species_by_fitness(self):
    for s in self.species:
      s.sort_players_by_fitness()

    self.species.sort(key=operator.attrgetter('benchmark_fitness'), reverse=True)

  def next_gen(self):
    # makes sure no birds from prior generations interfer with current
    # children are the birds that go to the next generation
    children = []

    #clone best player from each species
    for s in self.species:
      children.append(s.champion.clone())

    children_per_species = math.floor((self.size - len(self.species)) / len(self.species))
    for s in self.species:
      for i in range(0, children_per_species):
        children.append(s.offspring())

    while len(children) < self.size:
      children.append(self.species[0].offspring())

    self.players = []
    for child in children:
      self.players.append(child)
    self.generation += 1

  def extinct(self):
    extinct = True
    for player in self.players:
      if player.alive:
        extinct = False
    return extinct
  

  