import node
import connection
import random


class Brain:
  def __init__(self, inputs):
    self.connections = []
    self.nodes = []
    self.inputs = inputs
    self.net = []
    self.layers = 2

    for i in range(0, self.inputs):
      self.nodes.append(node.Node(i))
      self.nodes[i].layer = 0

    self.nodes.append(node.Node(3))
    self.nodes[3].layer = 0

    self.nodes.append(node.Node(4))
    self.nodes[4].layer = 1

    for i in range(0, 4):
      self.connections.append(connection.Connection(self.nodes[i], 
                                                    self.nodes[4], 
                                                    random.uniform(-1, 1)
                                                    ))
      
  def connect_nodes(self):
    for i in range(0, len(self.nodes)):
      self.nodes[i].connections = []

    for i in range(0, len(self.connections)):
      self.connections[i].from_node.connections.append(self.connections[i])

  def generate_net(self):
    self.connect_nodes()
    self.net = []
    for j in range(0, self.layers):
      for i in range(0, len(self.nodes)):
        if self.nodes[i].layer == j:
          self.net.append(self.nodes[i])

  def feed_forward(self, vision):
    for i in range(0, self.inputs):
      self.nodes[i].output_value = vision[i]

    self.nodes[3].output_Value = 1

    for i in range(0, len(self.net)):
      self.net[i].activate()

    output_value = self.nodes[4].output_value

    for i in range(0, len(self.nodes)):
      self.nodes[i].input_value = 0

    return output_value








