## @file BodyT.py
#  @author Simone Ocvirk
#  @brief defines the properties of a body
#  @date February 15th 2021

from Shape import Shape


## @brief defines the properties of a body
#  @details representions a body with properties center of mass x and y coordinates,
#   mass m, and moment
class BodyT(Shape):

    ## @brief Constructor for BodyT
    #  @param x is the x component of the center of mass
    #  @param y is the y component of the center of mass
    #  @param m is the mass
    def __init__(self, x, y, m):
        if len(x) != len(y) or len(x) != len(m) or len(y) != len(m):
            raise ValueError("lengths not equal")
        for i in m:
            if i <= 0:
                raise ValueError("not all masses are more than 0")
        self.__cmx = cmm(x, m)
        self.__cmy = cmm(y, m)
        self.__m = summ(m)
        self.__moment = mmomm(x, y, m) - summ(m) * (cmm(x, m)**2 + cmm(y, m)**2)

    ## @brief returns the x component of the center of mass
    #  @return cmx
    def cm_x(self):
        return self.__cmx

    ## @brief returns the y component of the center of mass
    #  @return cmy
    def cm_y(self):
        return self.__cmy

    ## @brief returns the mass
    #  @return m
    def mass(self):
        return self.__m

    ## @brief returns the moment
    #  @return moment
    def m_inert(self):
        return self.__moment


## @brief local function
#  @return summation
def summ(m):
    summation = 0
    for i in m:
        summation += i
    return summation


## @brief local function
#  @return center of mass
def cmm(z, m):
    total = 0
    for i in range(len(m)):
        total += z[i] * m[i]
    return total / summ(m)


## @brief local function
#  @return momemt
def mmomm(x, y, m):
    mom = 0
    for i in range(len(m)):
        mom += m[i] * ((x[i]**2) + (y[i]**2))
    return mom
