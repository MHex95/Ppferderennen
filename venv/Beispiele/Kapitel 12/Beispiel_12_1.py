# Beispiel 12.1
#
# Eine einfaches Beispiel zum Experimentieren
#
import Auto


def main():
    # Hauptprogramm
    auto_eins = Auto.Auto("Kia", "Silber", 50, 3)
    auto_zwei = Auto.Auto("Bentley", "Weiß", 150, 5)
    auto_drei = Auto.Auto("Fiat", "Rot", 120, 3)

    print("\nDaten von Auto eins:")
    auto_eins.zeige_daten()

    print("\nDaten von Auto zwei:")
    auto_zwei.zeige_daten()

    print("\nDaten von Auto drei:")
    auto_drei.zeige_daten()

    print("\nDie Autos fahren ein wenig durch die Gegend...")

    auto_eins.strecke_fahren(64)
    auto_zwei.strecke_fahren(128)
    auto_drei.strecke_fahren(110)

    print("Kilometerstand des ersten Autos:", auto_eins.kilometerstand)
    print("Kilometerstand des dritten Autos:", auto_drei.kilometerstand)
    print("wir haben Spaß!")
    print("asef")
    print("so ist es besser!!")
main()
