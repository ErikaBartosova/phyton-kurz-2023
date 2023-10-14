#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
import json

#Soubor si ulož a načti do slovníku.👇
with open("body.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#Vytvoř nový slovník.👇
prospech_dict = {}

#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
# Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".👇
for student, score in data.items():
    if score >= 60:
        prospech_dict[student] = "👍 Pass"
    else:
        prospech_dict[student] = "❌ Fail"

#Výsledný slovník ulož jako JSON do souboru prospech.json.

with open('prospech.json', 'w', encoding='utf-8') as output_file:
    json.dump(prospech_dict, output_file, ensure_ascii = False, indent = 4)
