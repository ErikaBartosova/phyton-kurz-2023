# Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

kod_soucastky = input("Zadejte prosím kód součástky: ")
mnozstvi = input("Zadejte prosím množství: ")
mnozstvi = int(mnozstvi)

if kod_soucastky in sklad:
    if sklad[kod_soucastky] >= mnozstvi:
        print(f"✅ Poptávku lze uspokojit v plné výši. Na skladě je aktuálně{sklad[kod_soucastky]} kusů.")
        sklad[kod_soucastky] -= mnozstvi
        print(f"Po objednávce na skladě zůstane {sklad[kod_soucastky]}.")
    else:
        print("❗ Lze prodat jen omezené množství kusů.")
else:
    print(f"❌ Bohužel, součástka {kod_soucastky} není skladem.")