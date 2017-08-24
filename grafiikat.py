import tkinter as tk
from tavara import *

hylly1 = hylly()

tavara1 = tavara("DMX", "piuha", "hylly1", 5)

hylly1.lisaaTavara(tavara1)


line0 = hylly1.getTavara(0)[0]

lista = line0.split(";")

print(lista[0])
