# 0x06. Python - Classes and Objects

This project focuses on understanding and implementing **classes** and **objects** in Python. It introduces the principles of Object-Oriented Programming (OOP) and how to apply them in Python.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the concept of OOP and its advantages.
- Define and use classes and objects in Python.
- Understand and implement instance attributes and methods.
- Differentiate between class attributes and instance attributes.
- Use special methods like `__init__` and `__str__`.
- Understand the concept of encapsulation and private attributes.

## Project Files

| File Name     | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| `0-square.py` | Defines an empty class `Square`.                                           |
| `1-square.py` | Adds a private instance attribute `size` to the `Square` class.            |
| `2-square.py` | Adds validation for the `size` attribute in the `Square` class.            |
| `3-square.py` | Adds a method to calculate the area of the square.                         |
| `4-square.py` | Adds getter and setter methods for the `size` attribute.                   |
| `5-square.py` | Adds a method to print the square using the `#` character.                 |
| `6-square.py` | Adds position attribute and modifies the print method to respect position. |

## Requirements

- Python 3.x
- Code should follow the [PEP 8](https://peps.python.org/pep-0008/) style guide.

## Usage

Each Python file can be executed independently to test the functionality of the corresponding class. Example:

```python
>>> from 3-square import Square
>>> sq = Square(3)
>>> print(sq.area())
9
```

## Author

This project is part of the ALX Higher-Level Programming curriculum.
