import config
import player

class Population:
  def __init__(self):
    self.player = player.Player()

  def update_players(self):
    if self.player.alive:
      self.player.think()
      self.player.update(config.ground)
      self.player.render(config.window)