import os

# Verzeichnis, in dem die .h-Dateien gespeichert sind
verzeichnis_pfad = '.'

# Name der Ausgabedatei
ausgabedatei = 'gesamte_datei.h'

# Oeffne die Ausgabedatei zum Schreiben
with open(ausgabedatei, 'w') as ausgabe:
    # Durchsuche das Verzeichnis nach .h-Dateien
    for datei_name in os.listdir(verzeichnis_pfad):
        if datei_name.endswith('.h'):
            # oeffne die aktuelle .h-Datei zum Lesen
            with open(os.path.join(verzeichnis_pfad, datei_name), 'r') as eingabe:
                # Lese den Inhalt der aktuellen .h-Datei
                datei_inhalt = eingabe.read()
                # Schreibe den Inhalt in die Ausgabedatei
                ausgabe.write(datei_inhalt)

print(f'Inhalt aller .h-Dateien wurde in {ausgabedatei} zusammengefasst.')
