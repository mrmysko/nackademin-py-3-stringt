[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/bBwanyKn)
# Uppgift 3 - Skapa den `print()`-liknande funktionen `stringt`

## Beskrivning

I denna uppgift ska du skapa en funktion med namnet `stringt` som liknar
beteendet hos den inbyggda funktionen `print()`, med den viktiga skillnaden att
`stringt` returnerar en sträng istället för att skriva ut den. Funktionen ska
kunna hantera ett valfritt antal positionella argument och stödja namngivna
argument för att anpassa textseparatorn och slutsträngen.

### Funktionsspecifikation

- **Funktionsnamn:** `stringt`
- **Positionella argument:** Ett valfritt antal, alla behandlas som strängar.
- **Namngivna argument:**
  - **sep (str, optional):** Anger textseparatorn som ska användas mellan varje
    argument. Standardvärdet är ett mellanslag `" "`.
  - **end (str, optional):** Anger en slutsträng som läggs till i slutet av den
    slutliga strängen. Standardvärdet är ett radmatningstecken `"\n"`.
- **Returvärde:** Funktionen ska returnera en sträng. Denna sträng består av
  alla positionella argument konverterade till strängar, sammanslagna med
  separatorn `sep` mellan varje argument, och med `end` lagt till i slutet.

Observera att `stringt()`-funktionen ska använda `return` för att returnera den
sammansatta strängen. Inga utskrifter med `print()` ska ske inuti funktionen.
Dessa exempel illustrerar hur stringt kan användas för att sammanfoga olika
strängar med valfri separator och avslutande tecken, liknande funktionen
`print()` men med skillnaden att `stringt()` returnerar den sammansatta strängen
istället för att skriva ut den.

1. **Exempel 1:**

   - **Input:** `stringt("Hej", "världen", sep=", ", end="!")`
   - **Förväntat resultat:** `"Hej, världen!"`
   - **Förklaring:** Argumenten "Hej" och "världen" sammanslås med separatorn ",
     " och avslutas med "!".

2. **Exempel 2:**

   - **Input:** `stringt("Python", "är", "kul")`
   - **Förväntat resultat:** `"Python är kul\n"`
   - **Förklaring:** Argumenten sammanslås med standardseparatorn " " och
     avslutas med standardvärdet för `end`, som är en radbrytning.

3. **Exempel 3:**

   - **Input:** `stringt("En", "två", "tre", sep=" - ")`
   - **Förväntat resultat:** `"En - två - tre\n"`
   - **Förklaring:** Argumenten sammanslås med separatorn " - " och avslutas med
     en radbrytning.

4. **Exempel 4:**

   - **Input:** `stringt("Slut", end=".")`
   - **Förväntat resultat:** `"Slut."`
   - **Förklaring:** Endast ett argument ges och funktionen avslutas med ".",
     som är det angivna värdet för `end`.

5. **Exempel 5:**

   - **Input:** `stringt("Ett", "argument", sep="")`
   - **Förväntat resultat:** `"Ettargument\n"`
   - **Förklaring:** Argumenten sammanslås utan någon separator och avslutas med
     en radbrytning.

6. **Exempel 6:**

   - **Input:** `stringt("Ensam")`
   - **Förväntat resultat:** `"Ensam\n"`
   - **Förklaring:** Endast ett argument ges och funktionen avslutas med
     standardvärdet för `end`, som är en radbrytning.

### Tips

När du arbetar med funktionen `stringt` för att sammanfoga strängar, kan
följande tips vara till hjälp:

1. För att skapa en sträng utifrån en lista med argument, kan du använda metoden
   [`str.join`](https://docs.python.org/3/library/stdtypes.html#str.join). Denna
   metod är effektiv för att sammanfoga en lista av strängar med en specifik
   separator.

2. Ibland kan dina argument vara av olika datatyper (till exempel, heltal eller
   flyttal). För att säkerställa att dessa kan sammanfogas utan problem, använd
   `str()`-funktionen för att konvertera alla argument till strängar innan
   sammanslagning.

Dessa tips kommer att underlätta skapandet av din `stringt`-funktion och hjälpa
dig att hantera olika typer av argument mer effektivt, samt att använda Python's
inbyggda funktioner för att skapa den slutgiltiga strängen.

### Inlämningsinstruktioner:

Din lösning ska innehålla funktionen `stringt` komplett med den beskrivna
funktionaliteten.

Inkludera kommentarer i din kod för att förklara din logik där det är
nödvändigt. Testa din funktion med flera olika input för att säkerställa att den
fungerar som förväntat och inkludera minst tre exempelkörningar (som de ovan) i
din inlämning.
