""" Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné,
s doménou czechitas.cz a tuto e-mailovou adresu vypíše.
Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz.
 """
Jméno = input("Vlož jméno: ")
mail= "@czechitas.cz"
výsledný_email = Jméno + mail
print(výsledný_email.lower())

