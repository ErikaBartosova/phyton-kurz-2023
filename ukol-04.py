import math
#Zeptá se uživatele na číslo, kam chce zprávu zaslat.

vložené_číslo = input("📞 Vložte prosím číslo příjemce: ")

#Ověří, že číslo má správný formát.

def ověření_čísla(vložené_číslo):
    počet_znaků = len(vložené_číslo)
    if počet_znaků == 9:
        return True
    elif počet_znaků == 13: #ověřit zda je vložená správná předvolba
        if vložené_číslo[:4] == "+420":
            return True
        else:
            return False
    else:
        return False

ověření_čísla(vložené_číslo)

# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
def délka_zprávy (vložená_zpráva):
    délka_textu = len(vložená_zpráva)
    cena = ((math.ceil(délka_textu / 180)) * 3)
    print(f"Cena ze SMS je {cena} Kč")
    return cena

################

if ověření_čísla(vložené_číslo) == True:
    vložená_zprváva = input("🗒️ Vložte text zrpávy: ")
    délka_zprávy(vložená_zprváva)
else:
    print("Vložené číslo osahuje chybu ⛔.")

