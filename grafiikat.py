import tkinter as tk
from tavara import *

#import tavara

# class Tietokanta():
#     def __init__(self, master):
#         frame = tk.Frame(master)
#         frame.pack()
#
#         self.tulostusNappi = tk.Button(frame, text="tulosta jotain", command=self.tulostaJotain)
#         self.tulostusNappi.pack(side=tk.LEFT)
#
#         self.poistu = tk.Button(frame, text="Poistu", command=frame.quit)
#         self.poistu.pack(side=tk.LEFT)
#
#
#     def tulostaJotain(self):
#         print("Jotain")

width = 960
height = 540

ikkuna = tk.Tk()

#tiet = Tietokanta(ikkuna)















# def leftClick(event):
#     print("left")
#
# def middleClick(event):
#     print("Middle")
#
# def rightClick(event):
#     print("Right")
#
# frame = tk.Frame(ikkuna, width=width, height=height)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()










hylly = hylly()
def lisaa(event, tavara):
    hylly.lisaaTavara(tavara)
    print("Tavara lisätty")

nimiText = tk.Label(ikkuna, text="Nimi")
tyyppiText = tk.Label(ikkuna, text="Tyyppi")
paikkaText = tk.Label(ikkuna, text="Paikka")
maaraText = tk.Label(ikkuna, text="Määrä")


nimi   = tk.Entry(ikkuna)
tyyppi = tk.Entry(ikkuna)
paikka = tk.Entry(ikkuna)
maara  = tk.Entry(ikkuna)

nimiText.grid(row=0, column=0, sticky=tk.E)
tyyppiText.grid(row=1, column=0, sticky=tk.E)
paikkaText.grid(row=2, column=0, sticky=tk.E)
maaraText.grid(row=3, column=0, sticky=tk.E)

nimi.grid(row=0, column=1)
tyyppi.grid(row=1, column=1)
paikka.grid(row=2, column=1)
maara.grid(row=3, column=1)

tavara = tavara(nimi, tyyppi, paikka, maara)

lisaaButton = tk.Button(ikkuna, text="Lisää",
                        command=lambda:lisaa(tavara))
lisaaButton.bind("<Button-1>")    # <Button-1> = Left Mouse Click eli se on eventti
lisaaButton.grid(row=4, column=1)
# Toinen tapa kutsua funktiota kun nappia painetaan
#kirjaudu = tk.Button(ikkuna, text="Kirjaudu", command=kirjautunut)


# valintaLaatikko = tk.Checkbutton(ikkuna, text="Pysy kirjautuneena")
# valintaLaatikko.grid(row=2, columnspan=2)


ikkuna.mainloop()
