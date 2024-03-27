import pytest


fn_name = "stringt"


class ImportDetailsError(Exception):
    pass


try:
    import uppgift

    fn = getattr(uppgift, fn_name)

    if not callable(fn):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    def test_exempel_1():
        assert fn("Hej", "världen", sep=", ", end="!") == "Hej, världen!"

    def test_exempel_2():
        assert fn("Python", "är", "kul") == "Python är kul\n"

    def test_exempel_3():
        assert fn("En", "två", "tre", sep=" - ") == "En - två - tre\n"

    def test_exempel_4():
        assert fn("Slut", end=".") == "Slut."

    def test_exempel_5():
        assert fn("Ett", "argument", sep="") == "Ettargument\n"

    def test_exempel_6():
        assert fn("Ensam") == "Ensam\n"

    def test_exempel_tomt_ensamt():
        assert fn("", sep="S", end="E") == "E"

    def test_exempel_tom_tva_tecken():
        assert fn("", "", sep="S", end="E") == "SE"

    def test_exempel_femton():
        arguments = list("c" * 15)
        sep = "SEPARATOR"
        end = "END"
        assert fn(*arguments, sep=sep, end=end) == sep.join(arguments) + end

    def test_exempel_femtio():
        arguments = list("woha" * 50)
        sep = "SEPARATOR"
        end = "END"
        assert fn(*arguments, sep=sep, end=end) == sep.join(arguments) + end

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")
