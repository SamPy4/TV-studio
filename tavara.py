class tavara():
    def __init__(self, nimi=None, tyyppi=None, paikka=None, maara=None):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.paikka = paikka
        self.maara = maara

    def getNimi(self):
        return self.nimi
    def setNimi(self, uusiNimi):
        self.nimi = uusiNimi
    def isNimi(self, nimi):
        return nimi == self.nimi.strip().lower()

    def getTyyppi(self):
        return self.tyyppi
    def setTyyppi(self, uusiTyyppi):
        self.tyyppi = uusiTyyppi
    def isTyyppi(self, tyyppi):
        return tyyppi == self.tyyppi

    def getPaikka(self):
        return self.paikka
    def setPaikka(self, uusiPaikka):
        self.paikka = uusiPaikka

    def getMaara(self):
        return self.maara
    def setMaara(self, uusiMaara):
        self.maara = uusiMaara
    def lisaa(self, maara):
        if self.maara + maara >= 0:
            self.maara += maara
        else: return
    def vahenna(self, maara):
        if self.maara - maara >= 0:
            self.maara -= maara
            return
        else: return

    def ota(self):
        if self.maara > 0:
            self.maara -= 1
        else:
            print("Ei voida ottaa, tavara loppu")
            return

    def toString(self):
        if self.maara == 1: muoto = "sitä"
        else: muoto = "niitä"
        return "{} on paikassa {} ja {} on {} kpl".format(self.nimi,
                                                          self.paikka,
                                                          muoto,
                                                          self.maara)

class hylly():
    def __init__(self):
        self.hylly = []

    def lisaaTavara(self, tavara):
        self.hylly.append(tavara)
        #print("Lisätty")

    def getTavara(self, index):
        return self.hylly[index].toString()

    def getKaikkiTavarat(self):
        string = ""

        for i in range(0, self.getTavaraMaara()):
            string += self.hylly[i].toString()
            if i == self.getTavaraMaara()-1:
                string += "\n"
            else:
                string += "\n\n"
        return string

    def getTavaraMaara(self):
        return len(self.hylly)

    def etsiNimella(self, tavara):
        tuloksia = 0
        esine = ""
        for i in range(0, self.getTavaraMaara()):
            if self.hylly[i].isNimi(tavara):
                esine = self.hylly[i].toString()
                tuloksia += 1
                break

        if tuloksia == 0:
            for i in range(0, self.getTavaraMaara()):
                if tavara in self.hylly[i].getNimi().strip().lower():
                    esine += self.hylly[i].toString()
                    esine += "\n"
            return "Hakutuloksia {} \n\nTarkoitit varmaan:\n{}\n".format(tuloksia,
                                                                         esine)
        return "Hakutuloksia {} \n\n{}\n".format(tuloksia,
                                              esine)

    def etsiTyypilla(self, tyyppi):
        esine = ""

        for i in range(0, self.getTavaraMaara()):
            if self.hylly[i].isTyyppi(tyyppi):
                esine += self.hylly[i].toString()
                esine += "\n"

        return esine

    def toString(self):
        #print("Printattu")
        string = ""

        return self.hylly[0].toString()

        #for i in range (0, len(self.hylly)):

def interface():
    print("""{}[1] - Etsi tavaroita nimellä
[2] - Etsi tavaroita tyypillä
[3] - Lisää tavara
[all] - Tulosta kaikki tavarat
[help] - Tulosta apu
[exit] - Poistu
{}
           """.format("-"*80,"-"*80))

"""
hylly = hylly()
dmx      = tavara("DMX-kaapeli", "johto", 1, 20)
adapteri = tavara("DVI-VGA-adapteri", "adapteri", 2, 10)
canon700 = tavara("Canon 700D", "kamera", 3, 1)
canon600 = tavara("Canon 600D", "kamera", 4, 2)
canon500 = tavara("Canon 500D", "kamera", 5, 4)
sd128    = tavara("128Gb SD-kortti", "muistikortti", 6, 0)

hylly.lisaaTavara(adapteri)
hylly.lisaaTavara(sd128)
hylly.lisaaTavara(dmx)
hylly.lisaaTavara(canon700)
hylly.lisaaTavara(canon500)
hylly.lisaaTavara(canon600)


interface()
while True:
    cmd = input(">>> ").strip().lower()

    if cmd == "1":
        etsittava = input("Nimi: ").strip().lower()
        print(hylly.etsiNimella(etsittava))
        continue

    if cmd == "2":
        etsittava = input("Tyyppi: ").strip().lower()
        print(hylly.etsiTyypilla(etsittava))
        continue

    if cmd == "3":
        print("njetnjet")
        continue

    if cmd == "help":
        interface()
        continue

    if cmd == "all":
        print(hylly.getKaikkiTavarat())
        continue

    if cmd == "":
        continue

    if cmd == "exit":
        break

print("Done")
"""
