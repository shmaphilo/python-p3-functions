#!/usr/bin/env python3
name="programmer!"
def greet_programmer():
    print(f"Hello, {name}")
    
def greet(name):
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1,num2):
    return num1 + num2

result=add(45,55)
print(result)


def halve(number):
    return number / 2
    
result=halve(10)
print(result)