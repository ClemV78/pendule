import tkinter as tk
import numpy as np
from equations import l, Newton, pas

theta0 = np.pi/4
thetap0 = 0
canvasx, canvasy = 500, 500
r = 50
l = 100*l
pas = int(1000*pas)
i_t = 0
tf = 10


def coords_cercle(r, theta):
    milieux = canvasx/2
    milieuy = canvasy/2
    return((int(milieux+l*np.sin(theta)-r), int(milieuy+l*np.cos(theta)-r), int(milieux+l*np.sin(theta)+r), int(milieuy+l*np.cos(theta)+r)))


fenetre = tk.Tk()

Bouton_Quitter = tk.Button(fenetre, text='Quitter', command=fenetre.destroy)
Bouton_Quitter.pack()

zone_dessin = tk.Canvas(fenetre, width=500, height=500, bg="white", bd=8)
zone_dessin.pack()

# Position initiale
milieux = canvasx/2
milieuy = canvasy/2
centre = zone_dessin.create_oval(
    milieux-2, milieuy-2, milieux+2, milieuy+2, fill='black')
aGi, oHi, aDi, oBi = coords_cercle(r, theta0)
balle = zone_dessin.create_oval(aGi, oHi, aDi, oBi, fill='red', width=10)
tige = zone_dessin.create_line(milieux, milieuy, zone_dessin.coords(balle)[
                               0]+r, zone_dessin.coords(balle)[1]+r, width=5)

l_t, l_y = Newton(tf, theta0, thetap0)


def deplacement():
    global i_t
    i_t += 1
    if i_t >= len(l_y):
        fenetre.destroy()
    else:
        aG, oH, aD, oB = coords_cercle(r, l_y[i_t])
        dx, dy = aG - \
            zone_dessin.coords(balle)[0], oH-zone_dessin.coords(balle)[1]
        zone_dessin.move(balle, dx, dy)
        aG, oH, a, o = zone_dessin.coords(balle)
        zone_dessin.coords(tige, (milieux, milieuy, aD-r, oB-r))
        fenetre.after(pas, deplacement)


deplacement()

fenetre.mainloop()
