# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.


def stringt(*args, end="\n", sep=" "):
    """Return a string."""

    # Creates strings from lists and ints from args and appends them to mod_list.
    mod_list = [str(i) for i in args]

    # Joins items in mod_list with sep as separator, concats end at the end.
    return sep.join(mod_list) + end

    # return return sep.join([str(i) for i in args]) + end # One-line


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    print(stringt("Det", "här", "är", "en", "sträng", end="1.", sep="-"))
    print(stringt("Det", "här", "är", "en", "sträng", end="2."))
    print(stringt("Det", "här", "är", "en", "sträng", sep="!"))
    print(stringt([1, 2, 3, 4], [5, 6, 7, 8], "Test", sep="F", end="4."))
    print(stringt(4, 5, 6, 7, 8, "Hej", sep=","))
    print(stringt((3, 5, 7, 9), ("Tuple"), ("LEL", "LOL"), sep="_", end="6."))
