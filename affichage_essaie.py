import tkinter as tk
dx = 0
dy = 5

fenetre = tk.Tk()

Bouton_Quitter = tk.Button(fenetre, text='Quitter', command=fenetre.destroy)
Bouton_Quitter.pack()

zone_dessin = tk.Canvas(fenetre, width=500, height=500, bg="white", bd=8)
zone_dessin.pack()

balle = zone_dessin.create_oval(200, 50, 300, 150, fill='red', width=10)


def deplacement():
    global dx, dy
    zone_dessin.move(balle, dx, dy)
    if zone_dessin.coords(balle)[3] >= 500 or zone_dessin.coords(balle)[1] <= 0:
        dy = -1 * dy
    fenetre.after(20, deplacement)


deplacement()

fenetre.mainloop()
