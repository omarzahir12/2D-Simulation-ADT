## @file CircleT.py
#  @author Simone Ocvirk
#  @brief defines the properties of a circle
#  @date February 15th 2021

from Shape import Shape


## @brief defines the properties of a circle
#  @details representions a circle with properties center of mass x and y coordinates,
#   radius r, and mass m
class CircleT(Shape):

    ## @brief Constructor for CircleT
    #  @param x is the x component of the center of mass
    #  @param y is the y component of the center of mass
    #  @param r is the radius
    #  @param m is the mass
    def __init__(self, x, y, r, m):
        if r <= 0 or m <= 0:
            raise ValueError("r and m are less than or equal to 0")
        self.__x = x
        self.__y = y
        self.__r = r
        self.__m = m

    ## @brief returns the x component of the center of mass
    #  @return x
    def cm_x(self):
        return self.__x

    ## @brief returns the y component of the center of mass
    #  @return y
    def cm_y(self):
        return self.__y

    ## @brief returns the mass
    #  @return m
    def mass(self):
        return self.__m

    ## @brief returns the inertia
    #  @return mr^2/2
    def m_inert(self):
        return (self.__m) * ((self.__r)**2) / 2
