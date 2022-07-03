import numpy as np
import matplotlib.pyplot as plt
g = 9.81
l = 2
w0 = np.sqrt(g/l)
pas = 0.02


def deriv(theta, thetap):
    return(thetap, -(w0**2)*np.sin(theta))


def Newton(tf, theta0, thetap0):
    x = [0]
    y = [[theta0, thetap0]]
    t = pas
    while t <= tf:
        x.append(t)
        theta, thetap = y[-1][0], y[-1][1]
        thetap1, thetapp1 = deriv(theta, thetap)
        y.append([theta + pas*thetap1, thetap + pas*thetapp1])
        t += pas
    return(x, [a[0] for a in y])


if __name__ == '__main__':
    x, y = Newton(10, np.pi/4, 0)
    plt.plot(x, y)
    plt.show()
