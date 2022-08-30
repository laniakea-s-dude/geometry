"""
   Ce programme permet :
   - d'afficher des figures géométriques (de tailles et de couleurs différentes)
   - de modifier leur position en les faisant glisser
   - de modifier leur couleur en cliquant dessus

   Mais il n'est pas orienté objet !
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
from random import random, randint
from matplotlib import colors
import six

# Une liste de couleurs
couleurs = [c[1] for c in list(six.iteritems(colors.cnames))]


def couleur_aleatoire():
    return couleurs[randint(0, len(couleurs)-1)]


def dimension_aleatoire(maxi=0.2):
    return max(0.1, maxi*random())


# Une figure, un système d'axes
fig, ax = plt.subplots()


ax.set_title('Faire glisser les formes ... ou changer leur couleur en cliquant')

# Des cercles
for i in range(5):
    ax.add_artist(mpatches.Circle((random(), random()), dimension_aleatoire(),
                                  color=couleur_aleatoire(),
                                  ec="none", picker=True))

# Des rectangles
for i in range(5):
    ax.add_artist(mpatches.Rectangle((random(), random()),
                                     dimension_aleatoire(0.4), dimension_aleatoire(0.4),
                                     color=couleur_aleatoire(),
                                     ec="none", picker=True))

# Variables globales
dx, dy = 0.0, 0.0  # Coordonnées relatives
ar = None  # artiste (forme géométrique)
mvt = False  # Pour indiquer qu'un mouvement a commencé


# Ce qui se produit quand une forme est sélectionnée
def quandChoix(event):
    global dx, dy, ar
    ar = event.artist

    if isinstance(ar, mpatches.Circle):
        xdata, ydata = ar.center
    elif isinstance(ar, mpatches.Rectangle):
        xdata, ydata = ar.xy
    dx, dy = event.mouseevent.xdata - xdata, event.mouseevent.ydata-ydata


# Ce qui se produit quand la souris se déplace
def quandMouvement(event):
    global mvt

    if event.inaxes is None:  # Le mouvement est en dehors du système d'axes
        return
    if event.button != 1:  # Le bouton de la souris n'est pas appuyé
        return
    if ar == None:  # Pas de forme sélectionnée
        return

    mvt = True  # Un mouvement a commencé
    x, y = event.xdata, event.ydata  # Les coordonnées de la souris

    if isinstance(ar, mpatches.Circle):
        ar.center = (x-dx, y-dy)

    elif isinstance(ar, mpatches.Rectangle):
        ar.set_x(x-dx)
        ar.set_y(y-dy)

    fig.canvas.draw()


# Ce qui se produit quand le bouton de la souris est relâché
def quandRelache(event):
    global ar, mvt
    if not mvt and ar is not None:
        ar.set_color(couleur_aleatoire())
        fig.canvas.draw()
    ar = None
    mvt = False


# Connection du canvas avec des événements
fig.canvas.mpl_connect('motion_notify_event', quandMouvement)
fig.canvas.mpl_connect('pick_event', quandChoix)
fig.canvas.mpl_connect('button_release_event', quandRelache)

plt.show()
