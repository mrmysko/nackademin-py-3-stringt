import pytest


class ImportDetailsError(Exception):
    pass


try:
    from uppgift import stringt

    if not callable(stringt):
        raise ImportDetailsError('Function "stringt" is not callable')

    # Kontrollera att stringt accepterar en variabel mängd argument Notera: Vi
    # kan inte enkelt kontrollera antalet positionella argument för en funktion
    # som accepterar *args, så vi hoppar över den kontrollen här.

    def test_exempel_1():
        assert stringt("Hej", "världen", sep=", ", end="!") == "Hej, världen!"

    def test_exempel_2():
        assert stringt("Python", "är", "kul") == "Python är kul\n"

    def test_exempel_3():
        assert stringt("En", "två", "tre", sep=" - ") == "En - två - tre\n"

    def test_exempel_4():
        assert stringt("Slut", end=".") == "Slut."

    def test_exempel_5():
        assert stringt("Ett", "argument", sep="") == "Ettargument\n"

    def test_exempel_6():
        assert stringt("Ensam") == "Ensam\n"

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    # Fail a test if the student has not implemented the function
    def test_import_fail():
        assert False, 'Funktionen "stringt" has not been implemented'
