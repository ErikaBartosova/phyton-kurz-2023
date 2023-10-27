# Mějme zadaný následující seznam naměřených teplot.
# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno [0], v poledne [1], večer [2] a v noci [3].

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvoř seznam průměrných teplot pro každý den.
prumerne_teploty = [round(sum(den) / len(den), 2) for den in teploty]
print(prumerne_teploty)

# Vytvoř seznam ranních teplot.
ranni_teploty = [den[0]for den in teploty]
print(ranni_teploty)

# Vytvoř seznam nočních teplot.
nocni_teploty = [den[3] for den in teploty]
print(nocni_teploty)

# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_nocni_teploty = [[den[1], den[3]] for den in teploty]
print(poledni_nocni_teploty)



############BONUS##############

#Krom teplot máme k dispozici i informaci o dnu v týdnu:

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
#{den: průměrná teplota}

prumerna_teplota = {den[0]: round(sum(den[1:]) / len(den[1:]), 2) for den in teploty}
print(prumerna_teplota)
