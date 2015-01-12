# Exercise 2: Cars and Hover Cars
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <Yan Zeng>, <zengyan>
#
# ---------------------------------------------
import math


class NotEnoughFuelError(Exception):
    pass


class Car:

    # Don't change this code!
    def __init__(self, fuel, efficiency):
        """ (Car, int, int) -> NoneType

        fuel is an int specifying the starting amount of fuel.
        efficiency is an int specifying how much fuel the car takes
        to travel 1 unit of distance.

        Initialize a new car with an amount of fuel and a fuel efficiency.
        The car's starting position is (0,0).
        """

        self.fuel = fuel
        self.efficiency = efficiency
        self.pos_x = 0
        self.pos_y = 0

    def move(self, new_x, new_y):
        """ (Car, int, int) -> NoneType

        Move the car from its old position to (new_x, new_y).
        Reduce the car's fuel depending on its efficiency and how far it
        travelled.

        If there isn't enough fuel to reach (new_x, new_y),
        do not change car's position or fuel level.
        Instead, raise NotEnoughFuelError.

        Remember that the car can only travel horizontally and vertically!
        """

        move_x = abs(new_x) - self.pos_x
        move_y = abs(new_y) - self.pos_y
        usedfuel = (move_x +  move_y) * self.efficiency
        
        if self.fuel >= usedfuel:
            self.fuel += -usedfuel
            self.pos_x = new_x
            self.pos_y = new_y
        else: 
            raise NotEnoughFuelError
               
        
class HoverCar(Car):

    def __init__(self, fuel, efficiency, hover_fuel):
        """ (HoverCar, int, int, int) -> NoneType

        hover_fuel is an int specifying the starting amount of hover fuel.

        Initialize a new HoverCar.
        """
        Car.__init__(self, fuel, efficiency)
        self.hover_fuel = hover_fuel

    def move(self, new_x, new_y):
        """ (HoverCar, int, int)

        Move the hover car according to the description in the exercise.
        Remember that hover cars try using regular fuel first,
        and only use hover fuel if there isn't enough regular fuel.

        Be sure to follow the implementation guidelines for full marks!
        """
        try:
            Car.move(self, new_x, new_y)
            
        except NotEnoughFuelError:
            print('Not enough regular fuel. Please use hover fuel.')
        
            moved_distance = math.sqrt((new_x - self.pos_x)**2 + (new_y - self.pos_y)**2)
            used_fuel = moved_distance / 20
            
            if self.hover_fuel >= used_fuel: 
                self.hover_fuel -= used_fuel
                self.hover_fuel = math.floor(self.hover_fuel)
                self.pos_x = new_x
                self.pos_y = new_y 
            else:
                raise NotEnoughFuelError
                
            
