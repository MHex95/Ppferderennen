import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

data = np.genfromtxt('Rockdata.txt', delimiter=',',
                     converters={-1: lambda s: 1.0 if s == b'M' else 0.0
                                 })

fulldata = np.insert(data, 0, 1, axis=1)
np.random.shuffle(fulldata)

testdata = fulldata[0:31, :]
training = fulldata[31:, :]

weights = np.random.rand(61)
epochen = 1000
alpha = 0.01

errors = [] # Liste für die Fehler

# Fortschrittsbalken
for epoche in tqdm(range(0, epochen)):

    error = 0 # Fehler zurücksetzen

    np.random.shuffle(training)

    # jeden Trainingsdatensatz präsentieren
    for i in range(0, len(training)):

        inputs = training[i, 0:61]
        target = training[i, -1]

        # Ergebnis des Perzeptron
        output = np.heaviside(inputs.dot(weights), 1.0)

        # Fehler ermitteln
        delta = target - output

        # Fehlschlag dokumentieren und Gewichte aktualisieren
        if (delta != 0):
            error += 1
            weights += delta * inputs * alpha # numpy benutzt automatisch Elementmultiplikation

    errors.append(error)

plt.figure(figsize=(12,5))
Trainingsfehler = plt.plot(errors)
_ = plt.title("Trainingsfehler über die Epochen", fontsize=16)

anzahl_fehler = 0

# Testdaten präsentieren
for test in testdata:

    o = np.heaviside(test[0:61].dot(weights), 1)

    delta = test[-1] - o

    # Fehler aufgetreten?
    if delta != 0.0:
        anzahl_fehler += 1

# Güte berechnen
anzahl_daten = len(testdata)
erkannte_daten = (anzahl_daten - anzahl_fehler) / anzahl_daten

print("Die Güte von dem Test: {0:.2f}".format(erkannte_daten))

plt.show()