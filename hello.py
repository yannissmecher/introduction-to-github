#!/usr/bin/env python3
"""
A simple Hello World program to demonstrate programming with Visual Studio Code.

This program demonstrates:
- Basic Python syntax
- Functions
- User input
- String formatting
"""


def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to GitHub and Visual Studio Code!"


def main():
    """Main function to run the program."""
    print("=" * 60)
    print("Welcome to your first program in Visual Studio Code!")
    print("=" * 60)
    print()
    
    # Get user input
    name = input("What is your name? ")
    
    # Display greeting
    message = greet(name)
    print()
    print(message)
    print()
    print("Happy coding! 🎉")


if __name__ == "__main__":
    main()
