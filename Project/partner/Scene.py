## @file Scene.py
#  @author Simone Ocvirk
#  @brief sets the scene
#  @date February 15th 2021
#  @details

# from Shape import Shape
from scipy.integrate import odeint


## @brief sets the scene
#  @details makes sure the vibes right
class Scene():

    ## @brief Constructor for BodyT
    #  @param s is a Shape
    #  @param Fx is the x component of the unbalanced force
    #  @param Fy is the y component of the unbalanced force
    #  @param vx is the x component of the velocity
    #  @param vy is the y component of the velocity
    def __init__(self, s, Fx, Fy, vx, vy):
        self.__s = s
        self.__Fx = Fx
        self.__Fy = Fy
        self.__vx = vx
        self.__vy = vy

    ## @brief returns the shape
    #  @return s
    def get_shape(self):
        return self.__s

    ## @brief returns the x and y components of the unbalanced force as a tuple
    #  @return (Fx, Fy)
    def get_unbal_forces(self):
        return (self.__Fx, self.__Fy)

    ## @brief returns the x and y components of the velocity as a tuple
    #  @return (vx, vy)
    def get_init_velo(self):
        return (self.__vx, self.__vy)

    ## @brief sets the shape as a new shape
    def set_shape(self, s):
        self.__s = s

    ## @brief sets the x and y components of the unbalanced force
    def set_unbal_forces(self, Fx, Fy):
        self.__Fx = Fx
        self.__Fy = Fy

    ## @brief sets the x and y components of the velocity
    def set_init_velo(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    ## @brief returns two sequences as a tuple
    #  @return (sequence1, sequence2)
    def sim(self, tf, steps):
        ## @brief local function
        #  @return something
        def ode(w, t):
            return (w[2], w[3], self.__Fx(t) / self.__s.mass(),
                    self.__Fy(t) / self.__s.mass())
        t = []
        for i in range(steps):
            t.append(i * tf / (steps - 1))
        return (t, odeint(ode, [self.__s.cm_x(), self.__s.cm_y(),
                self.__vx, self.__vy], t))
