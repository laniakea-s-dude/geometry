
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
from random import random, randint, uniform
from matplotlib import colors
import six


class RsizeColor:

    couleurs = [c[1] for c in list(six.iteritems(colors.cnames))]

    def __init__(self):
        pass

    @staticmethod
    def r_size():
        return max(0.1, 0.2 * random())

    @staticmethod
    def r_color():
        return RsizeColor.couleurs[randint(0, len(RsizeColor.couleurs)-1)]

    @staticmethod
    def r_angle():
        return uniform(0.0, 359.99)


class Ge00metricShapes:

    def __init__(self):
        self.rectangle = mpatches.Rectangle((random(), random()),
                                            RsizeColor.r_size(),
                                            RsizeColor.r_size(),
                                            RsizeColor.r_angle(),
                                            color=RsizeColor.r_color())
        self.circle = mpatches.Circle((random(), random()), RsizeColor.r_size(),
                                      color=RsizeColor.r_color())
        self.regpoly = mpatches.RegularPolygon((random(), random()),
                                               randint(3, 11),
                                               RsizeColor.r_size(),
                                               RsizeColor.r_angle(),
                                               color=RsizeColor.r_color())

    def pl00t(self):
        figure, axe = plt.subplots()
        for shape in (self.rectangle, self.circle, self.regpoly):
            axe.add_artist(shape)
        plt.show()


for i in range(5):
    g = Ge00metricShapes()
    print(vars(g))
    g.pl00t()