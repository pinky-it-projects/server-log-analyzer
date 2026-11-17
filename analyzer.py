import os

# stap: 1, logs Analyseren 
def analyseer_logs(log_map, rapport_map, bestandsnaam):
    aantal_error = 0
    aantal_critical = 0
    foutcodes = {}

    pad = os.path.join(log_map, bestandsnaam)

# Foutafhandeling met try / except
    try:
        with open(pad, "r", encoding="utf-8") as bestand:
            regels = bestand.readlines()

    except FileNotFoundError:
        print("Fout: Bestand niet gevonden!")
        return None
    
    pad_error = os.path.join(rapport_map, "error.txt")
    pad_critical = os.path.join(rapport_map, "critical.txt")
    
    with open(pad_error, "w", encoding="utf-8") as bestand_error, \
        open(pad_critical, "w", encoding="utf-8") as bestand_critical:
            for regel in regels:
                delen = regel.split("|")
                status = delen[1].strip()
                code = delen[2].strip().split()[0]

                if status == "ERROR":
                    aantal_error += 1
                    foutcodes[code] = foutcodes.get(code, 0) + 1
                    bestand_error.write(regel)
                elif status == "CRITICAL":
                    aantal_critical += 1
                    foutcodes[code] = foutcodes.get(code, 0) + 1
                    bestand_critical.write(regel)

    return aantal_error, aantal_critical, foutcodes

# stap: 2, Meeste voorkomende code zoeken
def meest_voorkomende_code(foutcodes):
    meeste_code = None
    hoogste_aantal = 0
    
    for code, aantal in foutcodes.items():
        if aantal > hoogste_aantal:
            hoogste_aantal = aantal
            meeste_code = code
    return meeste_code, hoogste_aantal

# stap: 3, Rapport schrijven
def schrijf_rapport(rapport_map, aantal_error, aantal_critical, foutcodes):
    meeste_code, hoogste_aantal = meest_voorkomende_code(foutcodes)

    pad_rapport = os.path.join(rapport_map, "rapport.txt")
    with open(pad_rapport, "w", encoding="utf-8") as bestand:
        bestand.write(f"ERROR: {aantal_error}\n")
        bestand.write(f"CRITICAL: {aantal_critical}\n")
        bestand.write(f"Meeste voorkomende code: {meeste_code} : {hoogste_aantal}")



# Stap: 4, Hoofdprogramma uitvoeren
# 4.1 Mappen instellen
log_map = "."
rapport_map = "."

# 4.2 Bestanden vragen
bestandsnaam = input("Voor de bestandsnaam in: ")

resultaat = analyseer_logs(log_map, rapport_map, bestandsnaam)

# 4.3 Resultaat controleren
if resultaat is not None:

# 4.4 Rapport uitpakken
    aantal_error, aantal_critical, foutcodes = resultaat

#4.5 Rapport genereren
    schrijf_rapport(rapport_map, aantal_error, aantal_critical, foutcodes)
    print("Analyse voltooid!")