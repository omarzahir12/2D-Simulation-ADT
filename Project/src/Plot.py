## @file Plot.py
#  @author Mohammad Omar Zahir, zahirm1
#  @brief This class implements the plot function to plot graphs from the data generated
#  by the Scene class.
#  @date Feb 11, 2021

import matplotlib.pyplot as plt


## @brief Method to plot the graph of various data values.
# @param w The window environment.
# @param t The set of time values.
# @throws ValueError When the length of the window environment is not the same as
# the data values for time, t
def plot(w, t):

    if not (len(w) == len(t)):
        raise ValueError
    x = []
    y = []
    for i in range(len(w)):
        x += [w[i][0]]
        y += [w[i][1]]
    fig, axs = plt.subplots(3)
    fig.suptitle('Motion Simulation')
    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(x, y)

    axs.flat[0].set(xlabel='t (m)', ylabel='x (m)')
    axs.flat[1].set(xlabel='t (m)', ylabel='y (m)')
    axs.flat[2].set(xlabel='x (m)', ylabel='y (m)')
    plt.subplots_adjust(hspace=0.5)
    plt.show()
