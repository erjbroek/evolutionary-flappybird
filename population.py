import config
import player

class Population:
  def __init__(self):
    self.player = player.Player()

  def update_players(self):
    self.player.render(config.window)