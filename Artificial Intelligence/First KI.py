import numpy as np
import random
# Funktion für Skalarprodukt
def skalarprodukt(liste1, liste2):
    '''
    Berechnet das Skalarprodukt über zwei Wertelisten.
    Listen müssen gleich lang sein.
    '''
    if len(liste1) != len(liste2):
        raise Exception("Listen müssen gleich lang sein")

    ergebnis = 0

    for i in range(len(liste1)):
        ergebnis = ergebnis + (liste1[i] * liste2[i])

    return ergebnis

# Heaviside Funktion
def heaviside(x):
    if x < 0:
        return 0
    else:
        return 1

training = [ [1.0, 1.0, 1.0 ], # Sonne scheint, Freunde haben Zeit
             [1.0, 0.0, 1.0,], # Freunde haben Zeit
             [1.0, 1.0, 0.0 ], # Sonne scheint
             [1.0, 0.0, 0.0 ]] # Gar nix von alledem

targets = [ 1.0, 0.0, 0.0, 0.0 ] # Das letzte war kein Schöner Tag

weights = [random.random() for i in range(0,3)]

print(weights)

alpha = 0.1
epochen = 100

indexes = [i for i in range(0,len(training))]

random.shuffle(indexes)

for e in range(0, epochen):
    print("Starte Epoche", e)
    for i in indexes:
        # Wir untersuchen genau ein Trainingsbeispiel
        inputs = training[i]
        target = targets[i]

        # Output o berechnen
        output = heaviside(skalarprodukt(inputs, weights))

        # Und das delta ermitteln zwischen Wunsch und Vorhersage des Perzeptron
        delta = target - output

        if (delta != 0):
            print("... Fehler erkannt bei Trainingsbeispiel {}".format(i))

        for n in range(0, len(weights)):
            weights[n] = weights[n] + delta * alpha * inputs[n]

print(weights)