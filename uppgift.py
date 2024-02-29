# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.


def stringt(*args, end="\n", sep=" "):
    """Return a string."""

    print(out_string)

    out_string = sep.join(args) + end
    return out_string


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
    print(stringt("Det", "här", "är", "en", "sträng", end=" ", sep="-"))
    print(stringt("Det", "här", "är", "en", "sträng"))
    print(stringt("Det", "här", "är", "en", "sträng", end="\t", sep="!"))
    # print(stringt([1, 2, 3, 4], [5, 6, 7, 8], sep="F"))
