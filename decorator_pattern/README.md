# Decorator Pattern in Python

This repository demonstrates the **Decorator Pattern**, a structural design pattern that allows behavior to be dynamically added to individual objects without affecting other objects of the same class. In this example, we create a simple beverage ordering system with decorators.
This repository contains Python code corresponding to Chapter 3 of the **“Head First Design Patterns”** book. The original code in the book is written in Java, and I’ve converted it to Python.
![decorator_pattern](./images/decorator_pattern.png)

## Key Features
The **Decorator Pattern** in object-oriented programming consists of the following key components:

1. **Component (Interface or Abstract Class)**:
   - Represents the base interface or abstract class that defines the common behavior for both the concrete component and its decorators.
   - Contains methods that the decorators can override or extend.
   - Acts as the foundation for the entire pattern.

2. **Concrete Component**:
   - Implements the `Component` interface or extends the `Component` abstract class.
   - Represents the actual object to which decorators can be added.
   - Provides the core functionality that decorators enhance.

3. **Decorator (Abstract Class)**:
   - Also known as the wrapper class.
   - Inherits from the `Component` interface or abstract class.
   - Contains a reference to the wrapped `Component`.
   - Defines additional behavior (decorators) that can be dynamically added to the component.
   - Forwards requests to the wrapped component and may modify the results.

4. **Concrete Decorator**:
   - Extends the `Decorator` class.
   - Adds specific functionality or behavior to the wrapped component.
   - Overrides methods from the `Component` interface or abstract class to customize behavior.
   - Can be stacked to create layered functionality.

The decorator pattern allows behavior to be added to an individual object dynamically, without affecting other instances of the same class. It promotes flexibility, adheres to the Single Responsibility Principle, and supports the Open-Closed Principle by allowing functionality extension without modifying existing code.

Remember that decorators and the original object share a common set of features, making it easy to stack multiple decorators on top of each other to create complex combinations.

## Example Use Case

Suppose you're building a coffee shop application that allows customers to customize their coffee orders. You want to apply the decorator pattern to **handle different types of coffee and additional condiments**.

1. **Base Coffee Types:**
   - You have three base coffee types: Espresso, House Blend Coffee, and Dark Roast Coffee.
   - Each coffee type has a description and a cost associated with it.

2. **Condiments:**
   - You also want to allow customers to add condiments to their coffee.
   - The condiments include Mocha, Whip, and Soy.
   - Each condiment modifies the description and cost of the coffee.

![decorator_pattern_example](./images/decorator_pattern_example.png)

3. **Applying the Decorator Pattern:**
   - You create an abstract base class called `Beverage`, which defines the basic structure for all coffee types.
   - Each specific coffee type (e.g., Espresso, House Blend, Dark Roast) extends the `Beverage` class and provides its own description and cost implementation.
   - The `CondimentDecorator` class extends `Beverage` and serves as the base class for all condiments.
   - Each condiment (e.g., Mocha, Whip, Soy) extends `CondimentDecorator` and modifies the description and cost of the wrapped beverage.

4. **Example Usage:**
   - You create an `Espresso` object and print its description and cost.
   - You create a `DarkRoast` object, add two `Mocha` condiments and one `Whip` condiment, and print the updated description and cost.
   - You create a `HouseBlend` object, add `Soy` and `Mocha` condiments, and print the final description and cost.

Here's how the scenario plays out:

```python
# Example usage
if __name__ == "__main__":
    # Create an Espresso
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    # Create a Dark Roast with condiments
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    # Create a House Blend with condiments
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))
```

In this scenario, the decorator pattern allows you to dynamically add and modify behavior (condiments) to the base coffee types without altering their core implementation. Customers can now enjoy customized coffee orders with various combinations of condiments! ☕🌟
