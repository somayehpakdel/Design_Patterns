# Factory Pattern

This repository is about **Factory Pattrn**. The content and code of this repository is inspired by Chapter 4 of the book " Head Frist Design Patterns". The original code is written in Java and I'v converted it to Python. 

This repository includes three ways to encapsulate object creation:

- **Simple Factory**
- **Factory Method**
- **Abstract Factory**

Each of these patterns is explained in their respective folders and is provided with Python code examples.

## Project structure
```
└── 📁factory_pattern
    └── README.md
    └── 📁abstract_factory
        └── README.md
        └── 📁images
        └── 📁src
    └── 📁factory_method
        └── README.md
        └── 📁images
        └── 📁src
    └── 📁simple_factory
        └── README.md
        └── 📁images
        └── 📁src
```

## Encapsulation of Object Creation
All factory patterns encapsulate the process of creating objects. This means that the details of how objects are created are hidden from the client, promoting a cleaner and more modular design.

### Simple Factory
While not officially recognized as a design pattern, the Simple Factory is a straightforward way to decouple clients from concrete classes. It involves a single method that returns instances of different classes based on input parameters. This approach simplifies object creation and reduces the dependency on specific classes.

### Factory Method
The Factory Method pattern relies on inheritance. Here, the creation of objects is delegated to subclasses, which implement the factory method to instantiate objects. This pattern allows a class to defer instantiation to its **subclasses**, promoting flexibility and scalability in the codebase.

### Abstract Factory
The Abstract Factory pattern uses object **composition** to create families of related objects without depending on their concrete classes. It defines an interface for creating objects, and the implementation of this interface is provided by concrete factory classes. This pattern is useful for creating objects that are designed to work together.


### Intent of Factory Method
The primary intent of the Factory Method pattern is to allow a class to defer the instantiation of objects to its subclasses*. This promotes code reuse and flexibility, as new types of objects can be introduced without modifying existing code.

### Intent of Abstract Factory
The Abstract Factory pattern aims to create families of related objects without relying on their concrete implementations. This ensures that the client code remains independent of the specific classes used to create objects, enhancing modularity and scalability.

## Dependency Inversion Principle in Factory Pattern
This principle advises us to avoid dependencies on concrete types and to strive for abstractions. By coding to interfaces rather than concrete classes, we can create more flexible and maintainable systems.

The Factory Pattern helps satisfy the Dependency Inversion Principle (DIP) by promoting the use of abstractions over concrete implementations. Here's how it works:

1. **Abstraction Over Implementation**: The Factory Pattern creates objects without specifying the exact class of the object that will be created. Instead, it relies on an interface or an abstract class. This means higher-level modules depend on abstractions rather than concrete classes, aligning with DIP.

2. **Decoupling**: By using a factory to create instances, the higher-level modules are decoupled from the lower-level modules. The factory handles the instantiation, allowing the higher-level modules to interact with interfaces or abstract classes, not concrete implementations.

3. **Flexibility and Maintainability**: The Factory Pattern allows for easy changes and extensions. If a new implementation is needed, it can be added without modifying the higher-level modules. This makes the system more flexible and easier to maintain.

In essence, the Factory Pattern helps invert the dependency direction, ensuring that high-level modules are not dependent on low-level modules but rather on abstractions, which is the core idea of the Dependency Inversion Principle.
