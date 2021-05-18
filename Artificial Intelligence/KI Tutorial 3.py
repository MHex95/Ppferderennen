import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from tqdm import tqdm


def verlust_absolut(target, output):
    return np.abs(target-output)


def verlust_quadrat(target, output):
    return (target - output)**2


def verlust_fuer_gewichte(verlustfunktion, w0, w1):

    fehler = 0.0

    for i in range(len(X)):

        output = X[i].dot(np.array([w0, w1]))

        target = y[i]

        fehler += verlustfunktion(target, output)

    return fehler


def verlust_fuer_grid(verlustfunktion, W0s, W1s):
    grid = []

    for w0 in W0s:
        ingrid = []

        for w1 in W1s:
            err = verlust_fuer_gewichte(verlustfunktion, w0, w1)
            ingrid.append(err)
        grid.append(ingrid)

    return np.array(grid)


def berechne_verlustfunktion(verlustfunktion):
    w0 = np.linspace(-10, 40, 40)
    w1 = np.linspace(-10, 40, 40)
    Z = verlust_fuer_grid(verlustfunktion, w0, w1)
    W0, W1 = np.meshgrid(w0, w1)

    return W0, W1, Z


def plotte_verlustfunktion(W0s, W1s, Z):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(11,11))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(W0s, W1s, Z, color='red', alpha=.8)
    ax.plot_wireframe(W0s, W1s, Z, color='y', alpha=0.2)
    ax.view_init(20, 35)
    ax.set_ylabel('w0', fontsize=16)
    ax.set_xlabel('w1', fontsize=16)
    ax.grid(True)
    ax.set_title('Verlust / Fehler', fontsize=16)


def gradientenabstieg(f, f_1, start_x, alpha, max_steps):
    """
    f ist die Funktion, die wir absteigen wollen
    f_1 ist die Ableitung dieser Funktion
    alpha ist unsere Lernrate
    max_steps ist die maximale Anzahl an Schritten
    """
    # Wir starten bei start_x
    pfad = [start_x]
    for step in range(0, max_steps):
        # Wie ist die Steigung an der Stelle start_x?
        steigung = f_1(start_x)

        # Wir machen eine Änderung entlang der Steigung
        aenderung_x = -1 * alpha * steigung

        # Und addieren die Änderung auf start_x
        # Wir haben dann einen neuen Startpunkt,
        # und wir können wieder von vorne beginnen
        start_x = start_x + aenderung_x

        # Wir merken uns die Reise von Punkt zu Punkt
        # damit wir diese später plotten können
        pfad.append(start_x)

    # Die Reise zurückgeben
    return pfad


def f_quadrat(x):
    return x ** 2


def f_quadrat_ableitung(x):
    return 2 * x


def plotte_gradientenabstieg(f, pfad):
    x = np.linspace(-6.5, 6.5, 100)
    plt.figure(figsize=(6, 8))

    # Zunaechst die Funktion einzeichnen
    plt.plot(x, f(x))
    ax = plt.gca()

    # Dann Pfeile einzeichnen für den Gradientenabstieg
    # OH DIESE PFEILE IN MATPLOTLIB!
    for i in range(0, len(pfad) - 1):
        posA = (pfad[i], f(pfad[i]))
        posB = (pfad[i + 1], f(pfad[i]))
        p = FancyArrowPatch(posA=posA, posB=posB,
                            arrowstyle='fancy, head_width=6, head_length=4',
                            color='red')
        ax.add_artist(p)
        posA = posB
        posB = (pfad[i + 1], f(pfad[i + 1]))
        p = FancyArrowPatch(posA=posA, posB=posB,
                            arrowstyle='fancy, head_width=6, head_length=4',
                            color='grey')
        ax.add_artist(p)


x = np.linspace(-10, 10, 100)
X = np.insert(x.reshape(100, 1), 0, 0, axis=1)
print(X.shape)

weights = np.zeros(2)
# ein wenig zufällige Werte erzeugen
y = 15 * x + 25 + np.random.randn(100) * 25

#W0s, W1s, Z = berechne_verlustfunktion(verlust_quadrat)
#plotte_verlustfunktion(W0s, W1s, Z)

pfad = gradientenabstieg(f_quadrat, f_quadrat_ableitung, 6, 0.85, 10)
#with plt.xkcd():

epochen = 250
alpha = 0.0001
errors = []
weigths = np.zeros(2)

plt.figure(figsize=(12, 9))
plt.scatter(X[:, 1], y, color='r')
plt.plot(X[:, 1], X.dot(weights), color='black', linestyle='--', alpha=.9)

data = list(zip(X, y))
for epoche in tqdm(range(0, epochen)):

    error = 0  # Um die Fehler für jede Epoche zu zählen

    # Einmal durchschütteln
    np.random.shuffle(data)

    # Für alle Datenpunkte...
    for i in range(0, len(X)):
        # Einmal das Netz aktivieren.
        inputs = data[i][0]
        output = inputs.dot(weights)  # ouput = mx + b

        # Was wäre unser Zieldatenpunkt in der Wolke gewesen?
        target = data[i][1]

        # Der Fehler ist unser quadratische Fehler
        error += verlust_quadrat(target, output)

        # Unsere magischer gewordene Delta-Regel
        # Da lineare Aktivierung, keine besondere Ableitung
        # einer Aktivierungsfunktion dazwischen
        weights += alpha * (target - output) * inputs

        # Jetzt haben wir für diese Epoche alle Datenpunkte präsentiert
    # und die Gewichte aktualisiert.

    # Wir merken uns den aufsummierten Fehler der Epoche
    errors.append(error)

    # Wir plotten die aktualisierte Linie in einem Blauton.
    # scale ist eine Hilfsvariable, um eine Skala auf den
    # Blautönen zu finden.
    scale = 1. - ((epochen - epoche) / epochen) / 2.
    plt.plot(X[:, 1], X.dot(weights), color=plt.cm.Blues(scale), alpha=0.8)

# Alle Epochen sind durch, wir plotten noch das finale Ergebnis
# in einem satten Blau
plt.plot(X[:, 1], X.dot(weights), color='b')
plt.grid(True)

# Wir setzen unser gefundenes mx+b in den Titel
_ = plt.title(str(weights[1]) + "x + " + str(weights[0]))
plt.show()
