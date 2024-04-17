import config
import player

class Population:
  def __init__(self, size):
    self.players = []
    self.size = size
    for i in range(0, self.size):
      self.players.append(player.Player())

  def update_players(self):
    for player in self.players:
      if player.alive:
        player.think()
        player.render(config.window)
        player.update(config.ground)

  def extinct(self):
    extinct = True
    for player in self.players:
      if player.alive:
        extinct = False
    return extinct
  