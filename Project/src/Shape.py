## @file Shape.py
#  @author Mohammad Omar Zahir, zahirm1
#  @brief This class acts as a blueprint interface module for Shapes to create other
# Shape classes.
#  @date Feb 11, 2021

from abc import ABC, abstractmethod


## @brief Creating an abstract data type for working with Shape objects and their
# basic properties. The methods are abstract and meant to be overwritten by the
# inheriting modules.
class Shape(ABC):

    ## @brief Method for determining the x-coordinate of the center of mass.
    @abstractmethod
    def cm_x(self):
        pass

    ## @brief Method for determining the y-coordinate of the center of mass.
    @abstractmethod
    def cm_y(self):
        pass

    ## @brief Method for determining the mass.
    @abstractmethod
    def mass(self):
        pass

    ## @brief Method for determining the moment of inertia.
    @abstractmethod
    def m_inert(self):
        pass
