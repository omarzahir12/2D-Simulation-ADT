## @file TriangleT.py
#  @author Simone Ocvirk
#  @brief defines the properties of a triangle
#  @date February 15th 2021

from Shape import Shape


## @brief defines the properties of a triangle
#  @details representions a triangle with properties center of mass x and y coordinates,
#   sidelength s, and mass m
class TriangleT(Shape):

    ## @brief Constructor for TriangleT
    #  @param x is the x component of the center of mass
    #  @param y is the y component of the center of mass
    #  @param s is the sidelength
    #  @param m is the mass
    def __init__(self, x, y, s, m):
        if s <= 0 or m <= 0:
            raise ValueError("s and m are less than or equal to 0")
        self.__x = x
        self.__y = y
        self.__s = s
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
    #  @return ms^2/12
    def m_inert(self):
        return (self.__m) * ((self.__s)**2) / 12
