# Strategy Pattern in Python

## Overview
This repository showcases an implementation of the strategy pattern using Python. The strategy pattern is a behavioral design pattern that allows clients to choose algorithms from a family of related algorithms dynamically. 
This repository contains Python code corresponding to Chapter 1 of the **“Head First Design Patterns”** book. The original code in the book is written in Java, and I’ve converted it to Python.
![strategy_pattern](./images/%20strategy_pattern.png)


## Implementation
In this example, we define the following components:

1. **Context (`Duck` class):** The object whose behavior will change based on the selected strategy.
2. **Strategies (`FlyBehavior` and `QuackBehavior` interfaces):** These represent different flying and quacking behaviors.

Each duck type inherits from the base `Duck` class and can dynamically change its flying and quacking behavior.

## Example Usage
```python
from src.duck import MallardDuck, ModelDuck

mallard = MallardDuck()
model = ModelDuck()

mallard.perform_fly()
model.perform_fly()

model.set_fly_behavior(FlyRocketPowered())
model.perform_fly()
```

In this example:
- We create instances of `MallardDuck` and `ModelDuck`.
- We invoke their `perform_fly()` methods to see how each duck behaves.
- For `ModelDuck`, we dynamically change its flying behavior to rocket-powered flight.

## Running the Simulation
To run this simulation:
1. Clone this repository.
2. Navigate to the source directory.
3. Run `python main.py`.
