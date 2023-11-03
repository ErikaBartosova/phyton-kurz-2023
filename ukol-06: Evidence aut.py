# Vytvoř třídu Auto, která bude obsahovat informace o autech
class Auto: 
        #Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.
    
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost=True): # informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota-True pokud je volné a False pokud je vypůjčené).
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost

    #Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. 
    def pujc_auto(self):
        if self.dostupnost:
            self.dostupnost = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    #tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla)
    def get_info(self):
        return f"Zvolili jste si auto {self.typ_vozidla} s poznávací značkou {self.registracni_znacka}."

auto_V1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
auto_V2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

volba_uzivatele = input("Přejete si zapůjčit automobil značky Škoda nebo Peugeot?: ")
volba_uzivatele = volba_uzivatele.lower()

if volba_uzivatele == "peugeot":
    if auto_V1.dostupnost:
        print(auto_V1.get_info())
        print(auto_V1.pujc_auto())
    else:
        print("Vozidlo není k dispozici.")
else:
    if volba_uzivatele == "škoda":
        if auto_V2.dostupnost:
            print(auto_V2.get_info())
            print(auto_V2.pujc_auto())
        else:
            print("Vozidlo není k dispozici.")
    else:
        print("Chybně zadaná značka automobilu")

# Otestuj, že program nedovolí půjčit stejné auto dvakrát.
""" volba_uzivatele = input("Přejete si zapůjčit automobil značky Škoda nebo Peugeot?: ")
volba_uzivatele = volba_uzivatele.lower()

if volba_uzivatele == "peugeot":
    if auto_V1.dostupnost:
        print(auto_V1.get_info())
        print(auto_V1.pujc_auto())
    else:
        print("Vozidlo není k dispozici.")
else:
    if volba_uzivatele == "škoda":
        if auto_V2.dostupnost:
            print(auto_V2.get_info())
            print(auto_V2.pujc_auto())
        else:
            print("Vozidlo není k dispozici.")
    else:
        print("Chybně zadaná značka automobilu")
 """
