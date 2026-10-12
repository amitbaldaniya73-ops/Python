"""
Data Abstraction :

    => To hide impletion detail from direct public user.

    1. Abstract Class
    2. Abstract Method


    1. Abstract Class
    -----------------

    => Cannot create object.
    => one or more than abstract method
    => To inherite ABC class


    2. Abstract Method
    -------------------

    => No any body
    => to use @abstractmethod

"""

# import abc
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog is Bhow Bhow...")


class Cat(Animal):

    def sound(self):
        print("Cat is moew, moew...")


obj = Dog()
obj.sound()


obj1 = Cat()
obj1.sound()
