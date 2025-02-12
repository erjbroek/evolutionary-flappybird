# Flappy Bird - Genetic Algorithm

This repository contains a Python implementation of a genetic algorithm applied to the Flappy Bird game using Pygame. The genetic algorithm is used to evolve a neural network that controls the bird's behavior in the game.

![flappy_bird_gif](https://github.com/user-attachments/assets/eca487a9-b6bb-4a69-8b0b-8bdb5a17b35b)

## Requirements

- Python 3.x
- Pygame

# Installation

You can install Pygame using pip, Python's package manager. Run the following command in your terminal or command prompt:

```bash
pip install pygame
```
<br></br>
# Overview
### The project consists of several components:

- **Player:** Represents the bird in the game. It has its own neural network (Brain) and handles interactions with the game environment.

- **Ground:** Represents the ground in the game.

- **Pipes:** Represents the obstacles (pipes) in the game.

- **Brain:** Contains the neural network implementation responsible for making decisions for the bird.

- **Population:** Manages a population of players, evolves them over generations using genetic algorithms, and handles species management.

- **Species:** Represents a group of players with similar neural networks. Helps maintain diversity within the population.

- **Nodes**: Individual nodes within the neural network, responsible for processing inputs and producing outputs.

- **Connections**: Connections between nodes in the neural network, representing weighted connections that transmit signals

<br></br>

# Genetic algoritm

**The genetic algorithm is used to evolve the neural networks of the birds (players) over several generations to improve their performance in the game. Here's a breakdown of the process:**

**Initialization:** A population of players is initialized, each with a unique neural network.

**Performance Evaluation:** Each player (**bird**) navigates through the game, and their performance (fitness) is evaluated based on the distance they travel and the number of pipes they successfully pass.

**Species Classification:** Players are grouped into **species** based on the similarity of their neural networks/ weights. This helps maintain diversity in the population by ensuring that different strategies are preserved.

**Selection:** Players within each **species** are sorted based on their performance. The higher the fitness score, the better their chances of survival and reproduction. The top performers in each **species** are selected to pass their genes to the next generation.

**Mutation:** To maintain genetic diversity and allow the algorithm to explore new solutions, random mutations are introduced in the offspring's neural networks. This involves changing weights.

**New Generation:** The new generation of players is created, consisting of offspring from the top performers of each **species** from the previous generation. This new generation then undergoes the same evaluation, **species** classification, selection, **crossover**, and **mutation** process.

<br></br>

## Usage

### To run the game:

Make sure you have Python and Pygame installed.
Clone the repository.
Navigate to the repository directory.
Run the main.py file.
```bash
python main.py
```
