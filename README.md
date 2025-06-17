# Asteroids

A simple implementation of the classic Asteroids game using [Pygame](https://www.pygame.org/).

## Installation

Install dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Game

Launch the game with:

```
python main.py
```

Use **WASD** to move and rotate the player ship, and **Space** to shoot.

## Files

- `main.py` – application entry point and main loop.
- `player.py` – player ship logic.
- `asteroids.py` – asteroid entity and splitting mechanics.
- `asteroidfield.py` – spawns asteroids over time.
- `shoots.py` – projectile logic.
- `circleshape.py` – common base class for circular game objects.
- `constants.py` – configurable values for gameplay and screen settings.
