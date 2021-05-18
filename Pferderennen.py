# Pferderennen

from random import randint
from math import sqrt


class Konto:
    def __init__(self, kontostand):
        self.kontostand = kontostand


class Jockey:
    def __init__(self, name, können):
        self.name = name
        self.können = können

    def zeige_jockey(self):
        print("Der Name des Jockeys:", self.name)


class Pferd:
    def __init__(self, startnummer, name, schnelligkeit, jockey):
        self.startnummer = startnummer
        self.name = name
        self.schnelligkeit = schnelligkeit
        self.jockey = jockey
        self.glück = None
        self.pech = None
        self.zeit = None

    def __str__(self):
        return "{0}: {1:.2f}".format(self.name, self.zeit)

    def berechne_quote(self, jockey):
        quote = 155 / (self.schnelligkeit + jockey.können) ** 1.5
        print("Quote: 1:{0:.2f}".format(quote))
        return quote

    def zeige_daten(self):
        print("\nPferd Nummer", self.startnummer, ":")
        print("Der Name des Pferdes: ", self.name)
        Jockey.zeige_jockey(self.jockey)
        self.berechne_quote(self.jockey)
        self.glück = randint(0, 20)
        self.pech = randint(0, 20)
        if self.glück > 16:
            print("------------------")
            print("{0} scheint heute gut drauf zu sein!".format(self.name))

    def rennen(self):
        strecke = 2500
        geschwindigkeit = (self.schnelligkeit + self.jockey.können) * 2 + 2 * self.glück + 2 * self.pech
        self.zeit = strecke / geschwindigkeit
        #print("Zeit {0}: {1:.2f}".format(self.name, self.zeit))
        return self.zeit

    def siegerehrung(self, reihenfolge, auswahl_pferd, betrag, wettkonto):
        if self == reihenfolge[0]:
            sieger = self.startnummer
            print("\nDer Sieger ist Pferd Nummer: {0}, '{1}'".format(self.startnummer, self.name))
            input()

            if auswahl_pferd == sieger:
                gewinn = betrag * self.berechne_quote(self.jockey)
                print("\nGewonnen! Sie erhalten {0:.2f} €".format(gewinn))
                wettkonto.kontostand += gewinn

                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))

            else:
                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))

            if sieger == 6:
                print("Ihr Pferd Gewinnt")
                wettkonto.kontostand += 500
                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))


def pferd_auswählen(pferde):
    while True:
        try:
            nummer_pferd = int(input("\nAuf welches Pferd wird gesetzt?: "))

        except ValueError:
            print("Eingabe ungültig!")
            continue

        if nummer_pferd > len(pferde) or nummer_pferd < 1:
            print("Dieses Pferd gibt es nicht!")

        else:
            break

    return nummer_pferd


def wetteinsatz(kontostand):
    while True:
        try:
            print("Ihr Kontostand: {0:.2f}".format(kontostand))
            betrag = float(input("Der Wetteinsatz: "))

        except ValueError:
            print("Eingabe ungültig!")
            continue

        if betrag > kontostand:
            print("So viel Geld besitzen Sie nicht!")

        else:
            return betrag


def pferd_kaufen():
    # Pferde werden vorgestellt
    print("\n1: Quirrly Whirly")
    preis1 = 200
    print("Preis: {0} €".format(preis1))
    print("Bewegt sich schnell, läuft aber langsam")

    print("\n2: Ross Anthony")
    preis2 = 1000
    print("Preis: {0} €".format(preis2))
    print("Zumindest ist er schön")

    print("\n3: Grand Grey")
    preis3 = 5000
    print("Preis: {0} €".format(preis3))
    print("War Champion in den 0er Jahren, hat die besten Zeiten hinter sich")

    print("\n4: Streitross")
    preis4 = 10000
    print("Preis: {0} €".format(preis4))
    print("Ein furchteinflößendes Tier, ein böser Blick und manch Gegner erstarrt")

    print("\n5: Chinesisches Pferd")
    preis5 = 100000
    print("Preis: {0}".format(preis5))
    print("Was machen die Chinesen bloß mit ihren Tieren?!")

    print("\nzum Abbrechen 0 wählen")

    while True:
        try:
            kauf_wahl = int(input("\nwelches Pferd möchten Sie kaufen? "))

        except ValueError:
            print("Ungültige Eingabe!")
            continue

        if 5 >= kauf_wahl >= 0:
            return kauf_wahl
        else:
            print("Dieses Pferd ist leider nicht verkäuflich")


def menu():
    # Ausgabe des Menüs:
    #
    while True:
        print("\n---------------------")
        print("Menü:")
        print("(Z)um Rennen")
        print("(P)ferdemarkt")
        print("(B)eenden")

    # Gewünschten Menüpunkt abfragen
    #
        auswahl = input("Deine Wahl: ")

        if auswahl == 'z' or auswahl == 'Z' or auswahl == 'b' or auswahl == 'B' or auswahl == 'p' or auswahl == 'P':
            return auswahl

        else:
            print('ungültige Eingabe')


def main():
    # Konto anlegen
    wettkonto = Konto(100)
    level = 1
    erfahrung = 0
    spieler = Jockey("Spieler", level)

    pferde = []

    # Pferde an den Start bringen
    jockey_eins = Jockey("Stefan Superschnell", 9)
    pferd_eins = Pferd(1, "Red Thunder", 9, jockey_eins)
    pferde.append(pferd_eins)

    jockey_zwei = Jockey("Sebastian Sporenhart", 8)
    pferd_zwei = Pferd(2, "Brutus", 7, jockey_zwei)
    pferde.append(pferd_zwei)

    jockey_drei = Jockey("Peter Pusteblume", 4)
    pferd_drei = Pferd(3, "Mister Hüh", 6, jockey_drei)
    pferde.append(pferd_drei)

    jockey_vier = Jockey("Holger Hinkelstein", 2)
    pferd_vier = Pferd(4, "Entchen", 4, jockey_vier)
    pferde.append(pferd_vier)

    jockey_fünf = Jockey("Bernd Blindfisch", 1)
    pferd_fünf = Pferd(5, "Ist das etwa ein Stein?!", 1, jockey_fünf)
    pferde.append(pferd_fünf)

    while True:
        auswahl = menu()

        if auswahl == 'Z' or auswahl == 'z':

            # Daten der Rennpferde
            print("\ndie Teilnehmer:")
            pferde.sort(key=lambda x: x.startnummer)
            for n in pferde:
                n.zeige_daten()

            # Wette platzieren
            auswahl_pferd = pferd_auswählen(pferde)
            betrag = wetteinsatz(wettkonto.kontostand)
            wettkonto.kontostand = wettkonto.kontostand - betrag

            print("\nEs wurden {0:.2f} € auf Pferd {1} gesetzt!".format(betrag, auswahl_pferd))

            input()
            # das Rennen!
            for n in pferde:
                n.rennen()

            pferde.sort(key=lambda x: x.zeit)

            for n in pferde:
                print(n)

            # Siegerermittlung und Gewinnausschüttung
            for n in pferde:
                n.siegerehrung(pferde, auswahl_pferd, betrag, wettkonto)

            if len(pferde) == 6:

                if pferd_sechs == pferde[0]:
                    erfahrung += 10
                else:
                    erfahrung += 1

                if erfahrung >= 10 * level ** 2 and level <= 10:
                    level += 1
                    print("\n+++++++++++++++++++++++++++++++")
                    print("Glückwunsch, Levelaufstieg!")
                    print("Ihr Level: {0}".format(level))
                    print("+++++++++++++++++++++++++++++++")
                    if level == 10:
                        print("\n+++++++++++++++++++++++++++++++++++++++")
                        print("Sie haben das höchste Level erreicht!!!")
                        print("+++++++++++++++++++++++++++++++++++++++++")

        if auswahl == 'P' or auswahl == 'p':
            auswahl_kauf = pferd_kaufen()

            if auswahl_kauf == 1:
                if wettkonto.kontostand < 200:
                    print("Nicht genug Geld!")

                else:
                    print("\nSie haben Quirrly Whirly erstanden!")
                    wettkonto.kontostand -= 200

                    if len(pferde) == 6:
                        pferde.remove(pferd_sechs)

                    pferd_sechs = Pferd(6, "Quirrly Whirly", 2, spieler)
                    pferde.insert(5, pferd_sechs)
                    input()

            if auswahl_kauf == 2:
                if wettkonto.kontostand < 1000:
                    print("Nicht genug Geld!")

                else:
                    print("\nSie haben Ross Anthony erstanden!")
                    wettkonto.kontostand -= 1000

                    if len(pferde) == 6:
                        pferde.remove(pferd_sechs)

                    pferd_sechs = Pferd(6, "Ross Anthony", 4, spieler)
                    pferde.insert(5, pferd_sechs)
                    input()

            if auswahl_kauf == 3:
                if wettkonto.kontostand < 5000:
                    print("Nicht genug Geld!")

                else:
                    print("\nSie haben Grand Grey erstanden!")
                    wettkonto.kontostand -= 5000

                    if len(pferde) == 6:
                        pferde.remove(pferd_sechs)

                    pferd_sechs = Pferd(6, "Grand Grey", 7, spieler)
                    pferde.insert(5, pferd_sechs)
                    input()

            if auswahl_kauf == 4:
                if wettkonto.kontostand < 10000:
                    print("Nicht genug Geld!")

                else:
                    print("\nSie haben Streitross erstanden!")
                    wettkonto.kontostand -= 10000

                    if len(pferde):
                        pferde.remove(pferd_sechs)

                    pferd_sechs = Pferd(6, "Streitross", 9, spieler)
                    pferde.insert(5, pferd_sechs)
                    input()

            if auswahl_kauf == 5:
                if wettkonto.kontostand < 100000:
                    print("Nicht genug Geld!")

                else:
                    print("\nSie haben Chinesisches Pferd erstanden!")
                    wettkonto.kontostand -= 100000

                    if len(pferde) == 6:
                        pferde.remove(pferd_sechs)

                    pferd_sechs = Pferd(6, "Chinesisches Pferd", 11, spieler)
                    pferde.insert(5, pferd_sechs)
                    input()

            #if auswahl_kauf == 0:
                #print("Dummy erzeugt")
                #pferd_sechs = Pferd(6, "Dummy", 1, spieler)
                #pferde.insert(5, pferd_sechs)

        if auswahl == 'b' or auswahl == 'B':
            print("Das Spiel wurde beendet")
            break

        if wettkonto.kontostand < 0.01:
            print("\n----------------------------------")
            print("Sie haben alles verloren!")
            print("Game Over")
            print("------------------------------------")
            break


main()